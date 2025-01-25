import unittest
import numpy as np
from pycuda_plus.utils.numpy_support import NumpyHelper
import pycuda.gpuarray as gpuarray

class TestNumpyHelper(unittest.TestCase):
    
    def test_array_conversion(self):
        """Test NumPy to PyCUDA array conversion."""
        helper = NumpyHelper()
        
        # Create a NumPy array
        array = np.array([1, 2, 3], dtype=np.float32)
        
        # Convert to GPU array
        gpu_array = helper.to_gpu(array)
        
        # Assert the GPU array is of the correct type
        self.assertIsInstance(gpu_array, gpuarray.GPUArray)
        
        # Check if the data in the GPU array matches the original NumPy array
        self.assertTrue(np.allclose(gpu_array.get(), array))

    def test_array_conversion_empty(self):
        """Test conversion of empty NumPy array to GPU."""
        helper = NumpyHelper()

        # Create an empty NumPy array
        array = np.array([], dtype=np.float32)

        # Convert to GPU array
        gpu_array = helper.to_gpu(array)

        # Assert the GPU array is also empty
        self.assertEqual(gpu_array.size, 0)

    def test_array_back_conversion(self):
        """Test converting from GPU back to NumPy array."""
        helper = NumpyHelper()

        # Create a NumPy array
        array = np.array([1, 2, 3], dtype=np.float32)

        # Convert to GPU and back to CPU
        gpu_array = helper.to_gpu(array)
        result = helper.to_cpu(gpu_array)

        # Check if the result matches the original array
        self.assertTrue(np.allclose(result, array))

if __name__ == "__main__":
    unittest.main()
