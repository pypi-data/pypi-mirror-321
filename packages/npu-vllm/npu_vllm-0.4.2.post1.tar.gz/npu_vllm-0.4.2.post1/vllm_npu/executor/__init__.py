from vllm_npu.executor.ray_utils import initialize_ray_cluster
from vllm.executor import ray_utils
ray_utils.initialize_ray_cluster = initialize_ray_cluster
