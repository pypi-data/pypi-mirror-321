from vllm.engine.llm_engine import LLMEngine
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm_npu.engine.ascend_engine import from_engine_args
from vllm_npu.engine.async_ascend_engine import from_engine_args_async
LLMEngine.from_engine_args = from_engine_args
AsyncLLMEngine.from_engine_args = from_engine_args_async
