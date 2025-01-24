from pycuda_plus.memory import allocate
from pycuda_plus.kernel import compile_kernel
from pycuda_plus.profiler import Profiler
from pycuda_plus.utils import generate_random_array, compare_arrays, print_array_summary

import numpy as np
import pycuda.driver as cuda
import logging

# Set up logging to include DEBUG messages
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG to see debug messages
logger = logging.getLogger("pycuda-plus-example")

device = cuda.Device(0)
max_threads_per_block = device.get_attribute(cuda.device_attribute.MAX_THREADS_PER_BLOCK)
logger.info(f"Max threads per block: {max_threads_per_block}")

# Initialize CUDA driver
cuda.init()
logger.info("CUDA driver initialized.")

# Step 1: Generate random data on the host
shape = (256, 256)
dtype = np.float64  # Use double precision to avoid floating-point precision issues
host_array = generate_random_array(shape, dtype, min_val=0.0, max_val=10.0)

# Make a copy of the host array to preserve the original
original_host_array = host_array.copy()

logger.info("Host array generated.")
print_array_summary(host_array, name="Host Array")

# Step 2: Allocate GPU memory and copy data to the GPU
gpu_array = allocate(shape, dtype)
gpu_array.copy_to_device(host_array)

logger.info("Data copied to GPU.")
logger.debug(f"First 10 elements on host (before copy): {host_array.flat[:10]}")

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

# Step 5: Launch the kernel with corrected grid and block size
block_size = (16, 16, 1)  # Threads per block
grid_size = (
    int(np.ceil(shape[0] * shape[1] / block_size[0])),  # Ensure full coverage of data
    1,
    1,
)  # Grid size based on total size

scale_factor = np.float64(2.0)

# Print the first 10 elements of host array before kernel execution
logger.debug(f"First 10 elements (host) before Profiler: {host_array.flat[:10]}")
logger.debug(f"Scale factor: {scale_factor}")

logger.debug(f"Block size: {block_size}, Grid size: {grid_size}")

# Run the kernel and profile its execution
execution_time = Profiler.time_kernel(
    scale_array_kernel,
    grid_size,
    block_size,
    gpu_array.gpu_buffer,  # Pass the GPU memory buffer
    scale_factor,
    np.int32(gpu_array.size)  # Total number of elements
)

logger.info(f"Kernel execution time: {execution_time:.4f} ms")

# Step 6: Synchronize to ensure kernel execution completes
cuda.Context.synchronize()  # Explicitly synchronize to ensure kernel completes
logger.info("CUDA context synchronized.")

# Step 7: Copy the data back to the host (scaled result)
result_array = gpu_array.copy_to_host()

# Print the first 10 elements of result_array (scaled)
logger.debug(f"First 10 elements in result_array (after kernel): {result_array.flat[:10]}")

# Print the first 10 elements of host_array (just to confirm)
logger.debug(f"First 10 elements of host_array (unchanged): {original_host_array.flat[:10]}")

# Print the expected result for comparison
expected_array = original_host_array * scale_factor
logger.debug(f"First 10 elements of expected_array (host * scale_factor): {expected_array.flat[:10]}")

# Compare the arrays and count matching vs non-matching
matching_count = 0
non_matching_count = 0

# Compare expected_array and result_array
try:
    compare_arrays(expected_array, result_array, atol=1e-4)  # Reasonable tolerance
    matching_count += 1
    logger.info("The kernel execution produced the expected results!")
except ValueError as e:
    non_matching_count += 1
    logger.error(f"Verification failed for expected vs result: {e}")

# Log the final count of matching vs non-matching arrays
logger.info(f"Arrays with no differences: {matching_count}")
logger.info(f"Arrays with differences: {non_matching_count}")

# Step 9: Free GPU memory
gpu_array.free()
logger.info("GPU memory freed.")
