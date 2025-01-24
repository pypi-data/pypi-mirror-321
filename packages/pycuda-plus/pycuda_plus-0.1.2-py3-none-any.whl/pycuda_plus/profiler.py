import pycuda.driver as cuda
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pycuda-plus-profiler")

class Profiler:
    """
    A utility class for profiling CUDA operations and kernel executions.
    """

    @staticmethod
    def time_kernel(kernel_function, grid, block, *args, stream=None, **kwargs):
        """
        Measure the execution time of a CUDA kernel.

        Args:
            kernel_function: The compiled CUDA kernel function.
            grid (tuple): Grid dimensions (number of blocks).
            block (tuple): Block dimensions (threads per block).
            *args: Positional arguments to pass to the kernel.
            stream (pycuda.driver.Stream, optional): CUDA stream for asynchronous execution.
            **kwargs: Keyword arguments (e.g., additional kernel parameters).

        Returns:
            float: Execution time in milliseconds.
        """
        start_event = cuda.Event()
        end_event = cuda.Event()

        start_event.record(stream)
        kernel_function(*args, block=block, grid=grid, stream=stream, **kwargs)
        end_event.record(stream)

        if stream:
            stream.synchronize()
        else:
            end_event.synchronize()

        elapsed_time = start_event.time_till(end_event)
        logger.info(f"Kernel execution time: {elapsed_time:.3f} ms")
        return elapsed_time

    @staticmethod
    def time_function(func, *args, **kwargs):
        """
        Measure the execution time of any Python function.

        Args:
            func: The function to time.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            float: Execution time in milliseconds.
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        logger.info(f"Function execution time: {elapsed_time:.3f} ms")
        return elapsed_time

    @staticmethod
    def profile_kernel(kernel_function, grid, block, iterations=10, *args, stream=None, **kwargs):
        """
        Profile a CUDA kernel by measuring its average execution time over multiple iterations.

        Args:
            kernel_function: The compiled CUDA kernel function.
            grid (tuple): Grid dimensions (number of blocks).
            block (tuple): Block dimensions (threads per block).
            iterations (int): Number of times to run the kernel for averaging.
            *args: Positional arguments to pass to the kernel.
            stream (pycuda.driver.Stream, optional): CUDA stream for asynchronous execution.
            **kwargs: Keyword arguments (e.g., additional kernel parameters).

        Returns:
            dict: A dictionary containing profiling results (min, max, avg execution time).
        """
        times = []
        for i in range(iterations):
            elapsed_time = Profiler.time_kernel(kernel_function, grid, block, *args, stream=stream, **kwargs)
            times.append(elapsed_time)

        profiling_results = {
            "min_time": min(times),
            "max_time": max(times),
            "avg_time": sum(times) / len(times),
        }
        logger.info(f"Kernel profiling results: {profiling_results}")
        return profiling_results

    @staticmethod
    def benchmark_kernels(kernel_configs, iterations=10):
        """
        Benchmark multiple kernels with different configurations.

        Args:
            kernel_configs (list): List of kernel configuration dictionaries, each containing:
                - "kernel_function": The CUDA kernel function.
                - "grid": Grid dimensions.
                - "block": Block dimensions.
                - "args": Positional arguments for the kernel (tuple).
                - "kwargs": Keyword arguments for the kernel (dict).
                - "stream": Optional CUDA stream.
            iterations (int): Number of iterations for each configuration.

        Returns:
            list: A list of results with kernel configurations and performance metrics.
        """
        results = []
        for config in kernel_configs:
            logger.info(f"Benchmarking kernel with grid={config['grid']} block={config['block']}")
            result = Profiler.profile_kernel(
                kernel_function=config["kernel_function"],
                grid=config["grid"],
                block=config["block"],
                iterations=iterations,
                *config.get("args", ()),
                stream=config.get("stream", None),
                **config.get("kwargs", {})
            )
            result["grid"] = config["grid"]
            result["block"] = config["block"]
            results.append(result)
        return results
