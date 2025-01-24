import pytest
import numpy as np
from pycuda_plus.memory import allocate
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test-memory")

def test_allocate_and_copy():
    logger.info("Testing memory allocation and data transfer.")
    shape = (256, 256)
    dtype = np.float32
    host_array = np.random.rand(*shape).astype(dtype)

    gpu_array = allocate(shape, dtype)
    gpu_array.copy_to_device(host_array)

    result_array = gpu_array.copy_to_host()

    assert np.allclose(host_array, result_array), "Data mismatch after GPU transfer"
    logger.info("Data transfer verification passed.")

    gpu_array.free()
    logger.info("GPU memory freed.")

def test_memory_cleanup():
    logger.info("Testing GPU memory cleanup.")
    shape = (128, 128)
    dtype = np.float32

    gpu_array = allocate(shape, dtype)
    gpu_array.free()

    try:
        gpu_array.free()
    except Exception as e:
        pytest.fail("Unexpected exception during memory cleanup: {}".format(e))
    logger.info("Memory cleanup test passed.")
