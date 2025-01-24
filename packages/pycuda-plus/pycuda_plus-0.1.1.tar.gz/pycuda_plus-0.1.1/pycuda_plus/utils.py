import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pycuda-plus-utils")

def generate_random_array(shape, dtype=np.float32, min_val=0.0, max_val=1.0):
    """
    Generate a random NumPy array with the specified shape and range.

    Args:
        shape (tuple): Shape of the array.
        dtype (data-type): Data type of the array. Default is np.float32.
        min_val (float): Minimum value of the random range.
        max_val (float): Maximum value of the random range.

    Returns:
        numpy.ndarray: A random array with the specified properties.
    """
    logger.info(f"Generating random array with shape={shape}, dtype={dtype}, range=({min_val}, {max_val})")
    array = np.random.uniform(low=min_val, high=max_val, size=shape).astype(dtype)
    logger.debug(f"Generated array: {array}")
    return array
def compare_arrays(array1, array2, atol=1e-5):
    """
    Compare two arrays element-wise with tolerance. Raise an error if they do not match.

    Args:
        array1 (numpy.ndarray): First array to compare.
        array2 (numpy.ndarray): Second array to compare.
        atol (float): Absolute tolerance for comparison. Default is 1e-5.

    Raises:
        ValueError: If the arrays have different shapes or do not match within the tolerance.

    Returns:
        bool: True if the arrays are equal within the tolerance, False otherwise.
    """
    logger.info("Comparing arrays...")

    # Check if arrays have the same shape
    if array1.shape != array2.shape:
        logger.error(f"Array shapes do not match! Array1 shape: {array1.shape}, Array2 shape: {array2.shape}")
        raise ValueError(f"Array shapes do not match! Array1 shape: {array1.shape}, Array2 shape: {array2.shape}")

    # Check if arrays are within tolerance
    if not np.allclose(array1, array2, atol=atol):
        # Log the absolute differences
        diff = np.abs(array1 - array2)

        # Find the indices where the differences are above tolerance
        diff_indices = np.where(diff > atol)
        logger.error("Arrays do not match within tolerance.")
        logger.debug(f"Difference (absolute values): {diff}")
        logger.debug(f"Indices where the arrays differ (absolute difference > {atol}): {diff_indices}")

        # Log a few sample differences
        for idx in zip(*diff_indices):
            logger.debug(f"Difference at index {idx}: Array1: {array1[idx]}, Array2: {array2[idx]}, Diff: {diff[idx]}")

        raise ValueError(f"Arrays do not match within the tolerance! Differences found at indices: {diff_indices}")

    logger.info("Arrays match within the specified tolerance.")
    return True

def reshape_array(array, new_shape):
    """
    Reshape a NumPy array to a new shape.

    Args:
        array (numpy.ndarray): The array to reshape.
        new_shape (tuple): The desired shape.

    Returns:
        numpy.ndarray: The reshaped array.
    """
    logger.info(f"Reshaping array from shape {array.shape} to {new_shape}")
    reshaped_array = np.reshape(array, new_shape)
    logger.debug(f"Reshaped array: {reshaped_array}")
    return reshaped_array

def print_array_summary(array, name="Array"):
    """
    Print a summary of a NumPy array, including shape, dtype, and basic stats.

    Args:
        array (numpy.ndarray): The array to summarize.
        name (str): Name of the array (for display purposes).
    """
    logger.info(f"Generating summary for {name}")
    summary = (
        f"{name} Summary:\n"
        f"  Shape: {array.shape}\n"
        f"  Data type: {array.dtype}\n"
        f"  Min: {np.min(array):.4f}, Max: {np.max(array):.4f}\n"
        f"  Mean: {np.mean(array):.4f}, Std: {np.std(array):.4f}"
    )
    logger.info(f"\n{summary}")
    print(summary)

def transfer_array_to_gpu(array):
    """
    Placeholder function for transferring a NumPy array to the GPU.

    Args:
        array (numpy.ndarray): The array to transfer.

    Returns:
        pycuda.gpuarray.GPUArray: GPU representation of the array (if PyCUDA integration is added).
    """
    logger.warning("transfer_array_to_gpu is not implemented yet.")
    pass

def transfer_array_from_gpu(gpu_array):
    """
    Placeholder function for transferring data from GPU to host.

    Args:
        gpu_array: The GPU array to transfer back.

    Returns:
        numpy.ndarray: Host representation of the array.
    """
    logger.warning("transfer_array_from_gpu is not implemented yet.")
    pass
