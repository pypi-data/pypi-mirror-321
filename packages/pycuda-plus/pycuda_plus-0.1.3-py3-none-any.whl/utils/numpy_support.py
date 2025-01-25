import pycuda.driver as cuda
import pycuda.gpuarray as gpuarray
import numpy as np

class NumpyHelper:
    """Utilities for integrating NumPy arrays with PyCUDA."""
    
    def __init__(self, device_id=0):
        """Initialize NumpyHelper instance and set up the CUDA context."""
        self.device_id = device_id
        cuda.init()  # Initialize the CUDA driver
        self.device = cuda.Device(self.device_id)  # Select the CUDA device
        self.context = self.device.make_context()  # Create a CUDA context
        print(f"CUDA device {self.device.name()} selected.")
    
    def to_gpu(self, numpy_array):
        """Convert a NumPy array to a PyCUDA device array."""
        return gpuarray.to_gpu(numpy_array)
    
    def to_cpu(self, device_array):
        """Convert a PyCUDA device array back to a NumPy array."""
        return device_array.get()

    def zeros_like(self, numpy_array):
        """Create a PyCUDA device array with the same shape as a NumPy array, initialized to zeros."""
        return gpuarray.zeros_like(self.to_gpu(numpy_array))

    def __del__(self):
        """Clean up the CUDA context when the helper object is deleted."""
        self.context.pop()  # Free the CUDA context
        print("CUDA context cleaned up.")

