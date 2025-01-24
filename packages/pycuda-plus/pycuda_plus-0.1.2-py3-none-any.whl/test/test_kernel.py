import numpy as np
import pycuda.driver as cuda
from pycuda_plus.memory import allocate
from pycuda_plus.kernel import compile_kernel
from pycuda_plus.profiler import Profiler
from pycuda_plus.utils import generate_random_array, compare_arrays, print_array_summary
import pytest
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test-kernel")

# Initialize CUDA driver
cuda.init()
logger.info("CUDA driver initialized.")

def test_compile_and_execute_kernel():
    logger.info("Testing kernel compilation and execution.")
    
    # Step 1: Generate random data on the host
    shape = (256, 256)
    dtype = np.float64
    host_array = generate_random_array(shape, dtype, min_val=0.0, max_val=10.0)

    logger.debug("Generated host array.")
    print_array_summary(host_array, name="Host Array")

    original_host_array = host_array.copy()
    
    # Step 2: Allocate GPU memory and copy data to the GPU
    gpu_array = allocate(shape, dtype)
    gpu_array.copy_to_device(host_array)

    logger.info("Data copied to GPU.")
    logger.debug(f"Host array (first 10 elements): {host_array.flat[:10]}")

    # Step 3: Define a simple CUDA kernel for scaling
    kernel_code = """
    __global__ void scale_array(double *array, double scale_factor, int size) {
        int idx = blockIdx.x * blockDim.x + threadIdx.x;
        if (idx < size) {
            array[idx] *= scale_factor;
        }
    }
    """
    # Step 4: Compile the kernel
    kernel_manager = compile_kernel(kernel_code)
    scale_array_kernel = kernel_manager.get_function("scale_array")
    logger.info("Kernel compiled successfully.")

    # Step 5: Launch the kernel
    block_size = (16, 16, 1)  # Threads per block
    grid_size = (
        int(np.ceil(shape[0] * shape[1] / block_size[0])),  # Ensure full coverage of data
        1,
        1,
    )  # Grid size based on total size

    scale_factor = np.float64(2.0)
    logger.debug(f"Block size: {block_size}, Grid size: {grid_size}")

    execution_time = Profiler.time_kernel(
        scale_array_kernel,
        grid_size,
        block_size,
        gpu_array.gpu_buffer,
        scale_factor,
        np.int32(gpu_array.size),
    )
    logger.info(f"Kernel execution time: {execution_time:.4f} ms")

    # Step 6: Synchronize and copy back results
    cuda.Context.synchronize()
    result_array = gpu_array.copy_to_host()

    # Print the expected result for comparison
    expected_array = original_host_array * scale_factor
 
    try:
        compare_arrays(expected_array, result_array, atol=1e-4)  # No assert, rely on exception if needed
        logger.info("Kernel execution produced expected results.")
    except ValueError as e:
        logger.error(f"Verification error: {e}")
        raise

    # Step 8: Free GPU memory
    gpu_array.free()
    logger.info("GPU memory freed.")

def test_invalid_kernel_execution():
    logger.info("Testing invalid kernel execution.")
    
    kernel_code = """
    __global__ void invalid_kernel(float *array) {
        int idx = blockIdx.x * blockDim.x + threadIdx.x;
        array[idx] = idx;
    }
    """
    kernel_manager = compile_kernel(kernel_code)
    invalid_kernel = kernel_manager.get_function("invalid_kernel")
    
    shape = (128,)
    dtype = np.float64
    gpu_array = allocate(shape, dtype)

    device = cuda.Device(0)
    max_threads_per_block = device.get_attributes().get(cuda.device_attribute.MAX_THREADS_PER_BLOCK)
    logger.info(f"Max threads per block: {max_threads_per_block}")

    block_size = (max_threads_per_block + 1, 1, 1)
    grid_size = (128, 1, 1)

    # Expecting an exception due to an invalid kernel execution
    with pytest.raises(cuda.Error, match="invalid argument"):
        invalid_kernel(gpu_array.gpu_buffer, block=block_size, grid=grid_size)
        logger.error("Expected kernel error did not occur.")

    gpu_array.free()
    logger.info("GPU memory freed after invalid kernel test.")
