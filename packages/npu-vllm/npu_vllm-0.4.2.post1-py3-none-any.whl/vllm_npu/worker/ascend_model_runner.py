# Copyright (c) Huawei Technologies Co., Ltd. 2024-2024. All rights reserved.
# Part of codes in this file was copied from project [vLLM Team][vllm]
from typing import List, NamedTuple, Optional, Tuple

import torch
from vllm.attention import AttentionMetadata, AttentionMetadataPerStage
from vllm.attention.backends.flashinfer import FlashInferBackend
from vllm.config import (
    DeviceConfig,
    LoadConfig,
    LoRAConfig,
    ModelConfig,
    ParallelConfig,
    SchedulerConfig,
    VisionLanguageConfig,
)
from vllm.distributed import broadcast_tensor_dict
from vllm.logger import init_logger
from vllm.lora.layers import LoRAMapping
from vllm.lora.request import LoRARequest
from vllm.model_executor import SamplingMetadata
from vllm.sampling_params import SamplingParams
from vllm.sequence import SamplerOutput, SequenceGroupMetadata
from vllm.utils import get_kv_cache_torch_dtype, is_hip, make_tensor_with_pad
from vllm.worker.model_runner import (
    _PAD_SLOT_ID,
    BatchType,
    ModelRunner,
    PrepareDecodeMetadata,
    PreparePromptMetadata,
    _prepare_fake_inputs,
)
from vllm_npu.model_executor.ascend_model_loader import get_model

logger = init_logger(__name__)
LORA_WARMUP_RANK = 8


class PreparePromptMetadata(NamedTuple):
    input_tokens: List[int]
    input_positions: List[int]
    attn_metadata: Optional[AttentionMetadataPerStage]
    seq_lens: List[int]
    query_lens: List[int]
    lora_index_mapping: List[int]
    lora_prompt_mapping: List[int]
    lora_requests: List[LoRARequest]
    multi_modal_input: Optional[torch.Tensor]
    slot_mapping: List[int]

    @classmethod
    def empty(cls):
        return PreparePromptMetadata(
            input_tokens=[],
            input_positions=[],
            attn_metadata=None,
            seq_lens=[],
            query_lens=[],
            lora_index_mapping=[],
            lora_prompt_mapping=[],
            lora_requests=[],
            multi_modal_input=None,
            slot_mapping=[],
        )


class PrepareDecodeMetadata(NamedTuple):
    input_tokens: List[int]
    input_positions: List[int]
    attn_metadata: Optional[AttentionMetadata]
    lora_index_mapping: List[int]
    lora_prompt_mapping: List[int]
    lora_requests: List[LoRARequest]
    slot_mapping: List[int]

    @classmethod
    def empty(cls):
        return PrepareDecodeMetadata(
            input_tokens=[],
            input_positions=[],
            attn_metadata=None,
            lora_index_mapping=[],
            lora_prompt_mapping=[],
            lora_requests=[],
            slot_mapping=[],
        )


class AscendModelRunner(ModelRunner):
    def __init__(
        self,
        model_config: ModelConfig,
        parallel_config: ParallelConfig,
        scheduler_config: SchedulerConfig,
        device_config: DeviceConfig,
        load_config: LoadConfig,
        lora_config: Optional[LoRAConfig],
        mindie_model_config,
        kv_cache_dtype: Optional[str] = "auto",
        is_driver_worker: bool = False,
        vision_language_config: Optional[VisionLanguageConfig] = None,
    ):
        super(AscendModelRunner, self).__init__(
            model_config,
            parallel_config,
            scheduler_config,
            device_config,
            load_config,
            lora_config,
            kv_cache_dtype,
            is_driver_worker,
            vision_language_config,
        )
        self.kv_cache_torch_dtype = get_kv_cache_torch_dtype(kv_cache_dtype, model_config.dtype)
        self.mindie_model_config = mindie_model_config
        self.mindie_model_config["kv_cache_dtype"] = self.kv_cache_torch_dtype

    def load_model(self) -> None:
        self.model = get_model(
            model_config=self.model_config,
            device_config=self.device_config,
            load_config=self.load_config,
            mindie_model_config=self.mindie_model_config,
        )

        if self.kv_cache_dtype == "fp8" and is_hip():
            # Currently scaled KV cache is only enabled on ROCm
            if self.model_config.quantization_param_path is not None:
                if callable(getattr(self.model, "load_kv_cache_scales", None)):
                    self.model.load_kv_cache_scales(self.model_config.quantization_param_path)
                else:
                    raise RuntimeError(
                        "Using FP8 KV cache and scaling factors provided but "
                        "model %s does not support loading scaling factors.",
                        self.model.__class__,
                    )
            else:
                logger.warning(
                    "Using FP8 KV cache but no scaling factors "
                    "provided. Defaulting to scaling factors of 1.0. "
                    "This may lead to less accurate results!"
                )
        elif self.model_config.quantization_param_path is not None:
            logger.warning(
                "KV cache scaling factors provided, "
                "but the KV cache data type is not FP8. "
                "KV cache scaling factors will not be used."
            )

    @torch.inference_mode()
    def profile_run(self) -> None:
        # Enable top-k sampling to reflect the accurate memory usage.
        sampling_params = SamplingParams(top_p=0.99, top_k=self.vocab_size - 1)
        max_num_batched_tokens = self.scheduler_config.max_num_batched_tokens
        max_num_seqs = self.scheduler_config.max_num_seqs

        dummy_lora_requests_per_seq = []

        seqs: List[SequenceGroupMetadata] = []

        if self.vision_language_config:
            max_num_seqs = min(
                max_num_seqs, int(max_num_batched_tokens / self.vision_language_config.image_feature_size)
            )
        for group_id in range(max_num_seqs):
            seq_len = max_num_batched_tokens // max_num_seqs + (group_id < max_num_batched_tokens % max_num_seqs)
            seq_data, fake_multi_modal_input = _prepare_fake_inputs(seq_len, self.vision_language_config)
            seq = SequenceGroupMetadata(
                request_id=str(group_id),
                is_prompt=True,
                seq_data={group_id: seq_data},
                sampling_params=sampling_params,
                block_tables=None,
                lora_request=dummy_lora_requests_per_seq[group_id] if dummy_lora_requests_per_seq else None,
                multi_modal_data=fake_multi_modal_input,
            )
            seqs.append(seq)

        # Run the model with the dummy inputs.
        num_layers = self.model_config.get_num_layers(self.parallel_config)
        kv_caches = [(None, None)] * num_layers
        self.execute_model(seqs, kv_caches)
        torch.npu.synchronize()
        return

    def _prepare_prompt(
        self,
        seq_group_metadata_list: List[SequenceGroupMetadata],
    ) -> PreparePromptMetadata:
        input_tokens: List[int] = []
        input_positions: List[int] = []
        slot_mapping: List[int] = []
        lora_index_mapping: List[int] = []
        lora_prompt_mapping: List[int] = []
        lora_requests: List[LoRARequest] = []

        seq_lens: List[int] = []
        context_lens: List[int] = []
        query_lens: List[int] = []
        prefix_block_tables: List[List[int]] = []
        multi_modal_input_list: List[torch.Tensor] = []

        if len(seq_group_metadata_list) == 0:
            return PreparePromptMetadata.empty()

        for seq_group_metadata in seq_group_metadata_list:
            if not seq_group_metadata.is_prompt:
                raise ValueError("Expected prompt sequence group metadata.")
            seq_ids = list(seq_group_metadata.seq_data.keys())
            if len(seq_ids) != 1:
                raise ValueError("Expected only one sequence ID.")
            seq_id = seq_ids[0]

            computed_block_nums = seq_group_metadata.computed_block_nums
            if (
                self.scheduler_config is not None
                and self.scheduler_config.chunked_prefill_enabled
                and not (computed_block_nums is None or computed_block_nums == [])
            ):
                raise RuntimeError("chunked prefill cannot be used with prefix caching " "now.")

            token_chunk_size = seq_group_metadata.token_chunk_size
            seq_data = seq_group_metadata.seq_data[seq_id]
            context_len = seq_data.get_num_computed_tokens()
            # We should use get_len here because in case of preemption
            # it contains output tokens.
            seq_len = min(seq_data.get_len(), context_len + token_chunk_size)
            prompt_tokens = seq_data.get_token_ids()[context_len:seq_len]
            seq_lens.append(seq_len)

            # NOTE: This only works for oooooooxxx style attention.
            if seq_group_metadata.block_tables is not None:
                block_table = seq_group_metadata.block_tables[seq_id]
            else:
                block_table = []
            if block_table:
                prefix_block_tables.append(block_table)
            else:
                prefix_block_tables.append([])
            if computed_block_nums is not None and len(computed_block_nums) > 0 and self.sliding_window is None:
                # Prefix is not supported with sliding_window
                context_len = len(computed_block_nums) * self.block_size
                prompt_tokens = prompt_tokens[context_len:]

            # actual prompt lens
            context_lens.append(context_len)
            query_lens.append(seq_len - context_len)

            input_tokens.extend(prompt_tokens)
            # NOTE(woosuk): Here we assume that the first token in the prompt
            # is always the first token in the sequence.
            input_positions.extend(list(range(context_len, seq_len)))
            lora_id = seq_group_metadata.lora_int_id

            lora_requests.append(seq_group_metadata.lora_request)

            lora_index_mapping += [lora_id] * (seq_len - context_len)
            lora_prompt_mapping.extend(
                [lora_id] * (seq_len - context_len if seq_group_metadata.sampling_params.prompt_logprobs else 1)
            )

            if seq_group_metadata.multi_modal_data:
                multi_modal_input_list.append(seq_group_metadata.multi_modal_data.data)

            if seq_group_metadata.block_tables is None:
                # During memory profiling, the block tables are not initialized
                # yet. In this case, we just use a dummy slot mapping.
                slot_mapping.extend([_PAD_SLOT_ID] * seq_len)
                continue

            # Compute the slot mapping.
            block_table = seq_group_metadata.block_tables[seq_id]

            # Mask the [0, start_idx) tokens of the prompt with _PAD_SLOT_ID,
            # where start_idx is max(0, seq_len - sliding_window).
            # For example, if the prompt len is 10, sliding window is 8, and
            # block size is 4, the first two tokens are masked and the slot
            # mapping will be [-1, -1, 2, 3, 4, 5, 6, 7, 0, 1].
            start_idx = 0
            if self.sliding_window is not None:
                if context_len != 0:
                    raise ValueError("Prefix caching is currently not supported with sliding window attention")
                start_idx = max(0, seq_len - self.sliding_window)

            for i in range(context_len, seq_len):
                if i < start_idx:
                    slot_mapping.append(_PAD_SLOT_ID)
                    continue

                block_number = block_table[i // self.block_size]
                block_offset = i % self.block_size
                slot = block_number * self.block_size + block_offset
                slot_mapping.append(slot)

        max_query_len = max(query_lens)
        max_seq_len = max(seq_lens)
        if max_query_len <= 0:
            raise ValueError("max_query_len must be greater than 0")

        context_lens_tensor = torch.tensor(context_lens, dtype=torch.int, device=self.device)

        if multi_modal_input_list:
            if not self.vision_language_config:
                raise ValueError("Multi-modal inputs are only supported by vision language models.")
            multi_modal_input = torch.cat(multi_modal_input_list, dim=0).to(self.device)
        else:
            multi_modal_input = None

        # Prepare prefix block tables
        max_prompt_block_table_len = max(len(t) for t in prefix_block_tables)
        block_tables = make_tensor_with_pad(
            prefix_block_tables,
            max_len=max_prompt_block_table_len,
            pad=0,
            dtype=torch.int,
            device=self.device,
        )

        # Query length can be shorter than key (i.e., prompt) when prefill
        # is chunked or prefix cached.
        query_lens_tensor = torch.tensor(query_lens, dtype=torch.long, device=self.device)
        subquery_start_loc = torch.zeros(query_lens_tensor.shape[0] + 1, dtype=torch.int32, device=self.device)

        seq_lens_tensor = torch.tensor(seq_lens, dtype=torch.int, device=self.device)
        seq_start_loc = torch.zeros(seq_lens_tensor.shape[0] + 1, dtype=torch.int32, device=self.device)

        torch.cumsum(query_lens_tensor, dim=0, dtype=subquery_start_loc.dtype, out=subquery_start_loc[1:])

        torch.cumsum(seq_lens_tensor, dim=0, dtype=seq_start_loc.dtype, out=seq_start_loc[1:])

        if self.attn_backend is FlashInferBackend:
            attn_metadata = self.attn_backend.make_metadata(
                is_prompt=True,
                use_cuda_graph=False,
                seq_start_loc=seq_start_loc,
                max_seq_len=max_seq_len,
                block_tables=block_tables,
            )
        else:
            attn_metadata = self.attn_backend.make_metadata(
                is_prompt=True,
                seq_lens=seq_lens,
                seq_lens_tensor=seq_lens_tensor,
                max_query_len=max_query_len,
                max_seq_len=max_seq_len,
                subquery_start_loc=subquery_start_loc,
                seq_start_loc=seq_start_loc,
                context_lens_tensor=context_lens_tensor,
                block_tables=block_tables,
                use_cuda_graph=False,
            )

        return PreparePromptMetadata(
            input_tokens=input_tokens,
            input_positions=input_positions,
            attn_metadata=attn_metadata,
            seq_lens=seq_lens,
            query_lens=query_lens,
            lora_index_mapping=lora_index_mapping,
            lora_prompt_mapping=lora_prompt_mapping,
            lora_requests=lora_requests,
            multi_modal_input=multi_modal_input,
            slot_mapping=slot_mapping,
        )

    def _prepare_decode(
        self,
        seq_group_metadata_list: List[SequenceGroupMetadata],
    ) -> PrepareDecodeMetadata:
        input_tokens: List[int] = []
        input_positions: List[int] = []
        slot_mapping: List[int] = []
        seq_lens: List[int] = []
        block_tables: List[List[int]] = []
        lora_index_mapping: List[int] = []
        lora_prompt_mapping: List[int] = []
        lora_requests: List[LoRARequest] = []


        if len(seq_group_metadata_list) == 0:
            return PrepareDecodeMetadata.empty()

        for seq_group_metadata in seq_group_metadata_list:
            if seq_group_metadata.is_prompt:
                raise ValueError("seq_group_metadata should not be a prompt")
            if seq_group_metadata.token_chunk_size != 1:
                raise ValueError("token_chunk_size should be 1")

            seq_ids = list(seq_group_metadata.seq_data.keys())
            lora_id = seq_group_metadata.lora_int_id

            lora_requests.append(seq_group_metadata.lora_request)

            for seq_id in seq_ids:
                seq_data = seq_group_metadata.seq_data[seq_id]
                generation_token = seq_data.get_last_token_id()
                input_tokens.append(generation_token)

                seq_len = seq_data.get_len()
                position = seq_len - 1
                input_positions.append(position)

                seq_len = seq_len if self.sliding_window is None else min(seq_len, self.sliding_window)
                seq_lens.append(seq_len)

                block_table = seq_group_metadata.block_tables[seq_id]
                block_number = block_table[position // self.block_size]
                block_offset = position % self.block_size
                slot = block_number * self.block_size + block_offset
                slot_mapping.append(slot)
                lora_index_mapping.append(lora_id)
                lora_prompt_mapping.append(lora_id)

                if self.sliding_window is not None:
                    sliding_window_blocks = self.sliding_window // self.block_size
                    block_table = block_table[-sliding_window_blocks:]
                block_tables.append(block_table)

        max_seq_len = max(seq_lens)
        seq_lens_tensor = torch.tensor(seq_lens, dtype=torch.int, device=self.device)

        max_block_table_len = max(len(block_table) for block_table in block_tables)
        block_tables = make_tensor_with_pad(
            block_tables,
            max_len=max_block_table_len,
            pad=0,
            dtype=torch.int,
            device=self.device,
        )

        attn_metadata = self.attn_backend.make_metadata(
            is_prompt=False,
            seq_lens=None,
            seq_lens_tensor=seq_lens_tensor,
            max_query_len=None,
            max_seq_len=max_seq_len,
            subquery_start_loc=None,
            seq_start_loc=None,
            context_lens_tensor=None,
            block_tables=block_tables,
            use_cuda_graph=False,
        )
        return PrepareDecodeMetadata(
            input_tokens=input_tokens,
            input_positions=input_positions,
            attn_metadata=attn_metadata,
            lora_index_mapping=lora_index_mapping,
            lora_prompt_mapping=lora_prompt_mapping,
            lora_requests=lora_requests,
            slot_mapping=slot_mapping,
        )

    def prepare_input_tensors(
        self,
        seq_group_metadata_list: List[SequenceGroupMetadata],
    ) -> Tuple[
        torch.Tensor, torch.Tensor, AttentionMetadata, SamplingMetadata, List[LoRARequest], LoRAMapping, torch.Tensor
    ]:
        if self.is_driver_worker:
            prefill_reqs = []
            decode_reqs = []
            for seq_group_meta in seq_group_metadata_list:
                if seq_group_meta.is_prompt:
                    prefill_reqs.append(seq_group_meta)
                else:
                    decode_reqs.append(seq_group_meta)

            # Prepare input tensors.
            (
                input_tokens,
                input_positions,
                prefill_attn_metadata,
                seq_lens,
                query_lens,
                lora_index_mapping,
                lora_prompt_mapping,
                lora_requests,
                multi_modal_input,
                slot_mapping,
            ) = self._prepare_prompt(prefill_reqs)
            (
                decode_input_tokens,
                decode_input_positions,
                decode_attn_metadata,
                decode_lora_index_mapping,
                decode_lora_prompt_mapping,
                decode_lora_requests,
                decode_slot_mapping,
            ) = self._prepare_decode(decode_reqs)
            sampling_metadata = SamplingMetadata.prepare(
                seq_group_metadata_list, seq_lens, query_lens, self.device, self.pin_memory
            )

            if not self.scheduler_config.chunked_prefill_enabled and prefill_reqs and decode_reqs:
                raise ValueError("Cannot have both prefill and decode requests when chunked_prefill_enabled is False")

            num_prefills = len(seq_lens)
            num_prefill_tokens = len(input_tokens)
            num_decode_tokens = len(decode_input_tokens)

            # Coalesce tensors. Note that attn_metadata is currently not
            # coalesced for simplicity.
            input_tokens.extend(decode_input_tokens)
            input_positions.extend(decode_input_positions)
            slot_mapping.extend(decode_slot_mapping)
            lora_index_mapping.extend(decode_lora_index_mapping)
            lora_prompt_mapping.extend(decode_lora_prompt_mapping)
            lora_requests.extend(decode_lora_requests)

            input_tokens = torch.tensor(input_tokens, dtype=torch.long, device=self.device)
            input_positions = torch.tensor(input_positions, dtype=torch.long, device=self.device)
            slot_mapping = torch.tensor(slot_mapping, dtype=torch.long, device=self.device)

            if self.lora_config:
                lora_mapping = LoRAMapping(
                    lora_index_mapping,
                    lora_prompt_mapping,
                )
            else:
                lora_mapping = None

            # Broadcast the metadata.
            # If batch contains both prefill and decode, it sends 2 broadcasts.
            # If it only contains 1 type, it triggers a single broadcast.
            if prefill_attn_metadata is not None and decode_attn_metadata is not None:
                batch_type = BatchType.MIXED
            elif prefill_attn_metadata is not None:
                batch_type = BatchType.PREFILL
            else:
                batch_type = BatchType.DECODE

            metadata_dict = {
                "input_tokens": input_tokens,
                "input_positions": input_positions,
                "selected_token_indices": sampling_metadata.selected_token_indices,
                "lora_requests": lora_requests,
                "lora_mapping": lora_mapping,
                "multi_modal_input": multi_modal_input,
                "num_prefill_tokens": num_prefill_tokens,
                "num_decode_tokens": num_decode_tokens,
                "slot_mapping": slot_mapping,
                "num_prefills": num_prefills,
                "batch_type": batch_type,
            }
            if prefill_attn_metadata is not None:
                metadata_dict.update(prefill_attn_metadata.asdict_zerocopy())
            else:
                if decode_attn_metadata is None:
                    raise ValueError("decode_attn_metadata is None")
                metadata_dict.update(decode_attn_metadata.asdict_zerocopy())
            broadcast_tensor_dict(metadata_dict, src=0)

            # Broadcast decode attn metadata for mixed batch type.
            # The additional broadcast costs 300us overhead on 4 A10 GPUs.
            # We can potentially reduce the overhead by coelescing tensors.
            if batch_type == BatchType.MIXED:
                if decode_attn_metadata is None:
                    raise ValueError("decode_attn_metadata is None")
                metadata_dict = decode_attn_metadata.asdict_zerocopy()
                broadcast_tensor_dict(metadata_dict, src=0)
        else:
            metadata_dict = broadcast_tensor_dict(src=0)
            input_tokens = metadata_dict.pop("input_tokens")
            input_positions = metadata_dict.pop("input_positions")
            slot_mapping = metadata_dict.pop("slot_mapping")
            num_prefills = metadata_dict.pop("num_prefills")
            selected_token_indices = metadata_dict.pop("selected_token_indices")
            lora_mapping = metadata_dict.pop("lora_mapping")
            lora_requests = metadata_dict.pop("lora_requests")
            multi_modal_input = metadata_dict.pop("multi_modal_input")
            num_prefill_tokens = metadata_dict.pop("num_prefill_tokens")
            num_decode_tokens = metadata_dict.pop("num_decode_tokens")
            batch_type = metadata_dict.pop("batch_type")

            # Create an attention metadata.
            prefill_attn_metadata = None
            decode_attn_metadata = None
            if batch_type == BatchType.PREFILL or batch_type == BatchType.MIXED:
                prefill_attn_metadata = self.attn_backend.make_metadata(**metadata_dict)
            else:
                decode_attn_metadata = self.attn_backend.make_metadata(**metadata_dict)
            sampling_metadata = SamplingMetadata(
                seq_groups=None,
                selected_token_indices=selected_token_indices,
                categorized_sample_indices=None,
                num_prompts=0,
            )

            # if it is a mixed batch, decode attn_metadata is broadcasted
            # separately.
            if batch_type == BatchType.MIXED:
                metadata_dict = broadcast_tensor_dict(src=0)
                decode_attn_metadata = self.attn_backend.make_metadata(**metadata_dict)

        attn_metadata = AttentionMetadata(
            num_prefills=num_prefills,
            slot_mapping=slot_mapping,
            num_prefill_tokens=num_prefill_tokens,
            num_decode_tokens=num_decode_tokens,
            prefill_metadata=prefill_attn_metadata,
            decode_metadata=decode_attn_metadata,
            kv_cache_dtype=self.kv_cache_torch_dtype,
        )

        return (
            input_tokens,
            input_positions,
            attn_metadata,
            sampling_metadata,
            lora_requests,
            lora_mapping,
            multi_modal_input,
        )

    @torch.inference_mode()
    def execute_model(
        self,
        seq_group_metadata_list: List[SequenceGroupMetadata],
        kv_caches: List[Tuple[torch.Tensor, torch.Tensor]],
    ) -> Optional[SamplerOutput]:
        (input_tokens, input_positions, attn_metadata, sampling_metadata, lora_requests, _, _) = (
            self.prepare_input_tensors(seq_group_metadata_list)
        )

        # Currently cuda graph is only supported by the decode phase.
        model_executable = self.model
        execute_model_kwargs = {
            "input_ids": input_tokens,
            "positions": input_positions,
            "kv_caches": kv_caches,
            "attn_metadata": attn_metadata,
            # "lora_requests": lora_requests,
        }
        hidden_states = model_executable(**execute_model_kwargs)

        # Only perform sampling in the driver worker.
        if not self.is_driver_worker:
            return None

        # Sample the next token.
        output = self.model.sample(
            logits=hidden_states,
            sampling_metadata=sampling_metadata,
        )

        return output