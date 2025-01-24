import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pycuda-plus")

class MemoryAllocationError(Exception):
    pass

class GPUArray:
    """
    A high-level abstraction for GPU memory management with PyCUDA.
    """

    def __init__(self, shape, dtype=np.float32):
        """
        Initialize GPU memory for a given shape and dtype.

        Args:
            shape (tuple): Shape of the array.
            dtype (data-type): Data type of the array. Default is np.float32.
        """
        self.shape = shape
        self.dtype = dtype
        self.size = np.prod(shape)
        self.host_array = np.zeros(shape, dtype=dtype)
        try:
            self.gpu_buffer = cuda.mem_alloc(self.host_array.nbytes)
            logger.info(f"Allocated GPU memory: {self.host_array.nbytes} bytes")
        except cuda.MemoryError as e:
            logger.error("Failed to allocate GPU memory", exc_info=True)
            raise MemoryAllocationError(f"Failed to allocate GPU memory: {e}")
        self.is_freed = False

    def copy_to_device(self, host_array, stream=None):
        """
        Copy data from host (CPU) to device (GPU).

        Args:
            host_array (numpy.ndarray): Data to copy to the GPU.
            stream (pycuda.driver.Stream, optional): CUDA stream for asynchronous copy.
        """
        if host_array.shape != self.shape:
            raise ValueError(f"Shape mismatch: Expected shape {self.shape}, got shape {host_array.shape}")
        if stream:
            cuda.memcpy_htod_async(self.gpu_buffer, host_array, stream)
            logger.info("Data copied to GPU (async mode)")
        else:
            cuda.memcpy_htod(self.gpu_buffer, host_array)
            logger.info("Data copied to GPU")
        self.host_array = host_array

    def copy_to_host(self, stream=None):
        """
        Copy data from device (GPU) back to host (CPU).

        Args:
            stream (pycuda.driver.Stream, optional): CUDA stream for asynchronous copy.

        Returns:
            numpy.ndarray: Data copied back from the GPU.
        """
        if stream:
            cuda.memcpy_dtoh_async(self.host_array, self.gpu_buffer, stream)
            logger.info("Data copied to host (async mode)")
        else:
            cuda.memcpy_dtoh(self.host_array, self.gpu_buffer)
            logger.info("Data copied to host")
        return self.host_array

    def free(self):
        """
        Free the GPU memory buffer.
        """
        if not self.is_freed:
            self.gpu_buffer.free()
            self.is_freed = True
            logger.info("Freed GPU memory")

    def __del__(self):
        """
        Automatically free GPU memory when the object is deleted.
        """
        try:
            self.free()
        except cuda.LogicError:
            logger.warning("GPU memory already freed or invalid resource handle")


class GPUMemoryPool:
    """
    A memory pooling mechanism to reduce allocation overhead.
    """
    def __init__(self):
        self.pool = {}

    def allocate(self, shape, dtype=np.float32):
        size = np.prod(shape) * np.dtype(dtype).itemsize
        if size in self.pool and self.pool[size]:
            logger.info("Reusing memory from pool")
            return self.pool[size].pop()
        else:
            logger.info("Allocating new GPU memory")
            return GPUArray(shape, dtype)

    def free(self, gpu_array):
        size = gpu_array.host_array.nbytes
        if size not in self.pool:
            self.pool[size] = []
        self.pool[size].append(gpu_array)
        logger.info("Returned memory to pool")

    def clear(self):
        """
        Clear all memory from the pool.
        """
        self.pool = {}
        logger.info("Cleared memory pool")


# Utility function for allocation
def allocate(shape, dtype=np.float32):
    """
    Allocate GPU memory for a given shape and dtype.

    Args:
        shape (tuple): Shape of the array.
        dtype (data-type): Data type of the array.

    Returns:
        GPUArray: A GPUArray object managing the allocated memory.
    """
    return GPUArray(shape, dtype)
