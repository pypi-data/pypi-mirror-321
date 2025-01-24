import pycuda.driver as cuda
import pycuda.compiler as compiler
import hashlib
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pycuda-plus")

class KernelCompilationError(Exception):
    pass


class KernelManager:
    """
    A class to manage the compilation, execution, and retrieval of CUDA kernels.
    
    This class compiles CUDA kernel source code, allows retrieval of compiled 
    kernel functions and PTX code, and manages errors during compilation.

    Args:
        kernel_source (str): The CUDA kernel source code as a string.

    Methods:
        compile(options=None):
            Compiles the CUDA kernel source code using the provided options.
        
        get_function(function_name):
            Retrieves the compiled kernel function by its name.
        
        get_ptx():
            Retrieves the PTX code from the compiled module.
    
    Raises:
        KernelCompilationError: If kernel compilation fails.
    """

    def __init__(self, kernel_source):
        """
        Initializes the KernelManager instance with the kernel source code.

        Args:
            kernel_source (str): The CUDA kernel source code as a string.
        """
        self.kernel_source = kernel_source
        self.module = None


    def compile(self, options=None):
        """
        Compile the CUDA source code.

        Args:
            options (list): Additional compiler options (e.g., ['--use_fast_math']).
        """
        try:
            logger.info("Compiling CUDA kernel")
            self.module = compiler.SourceModule(self.kernel_source, options=options)
            logger.info("CUDA kernel compilation successful")
        except compiler.CompileError as e:
            logger.error("CUDA kernel compilation failed", exc_info=True)
            raise KernelCompilationError(f"Kernel compilation failed: {e}")

    def get_function(self, function_name):
        """
        Retrieve a compiled CUDA function.

        Args:
            function_name (str): The name of the kernel function.

        Returns:
            pycuda.driver.Function: The compiled CUDA kernel function.
        """
        if self.module is None:
            logger.error("Kernel source has not been compiled. Call compile() first.")
            raise RuntimeError("Kernel source has not been compiled. Call compile() first.")
        logger.info(f"Retrieved function '{function_name}' from compiled module")
        return self.module.get_function(function_name)

    def get_ptx(self):
        """
        Retrieve the compiled PTX code for the kernel.

        Returns:
            str: The PTX code as a string.
        """
        if self.module is None:
            logger.error("Cannot retrieve PTX. Kernel source has not been compiled.")
            raise RuntimeError("Kernel source has not been compiled. Call compile() first.")
        logger.info("PTX code retrieved")
        return self.module.get_ptx()


class KernelCache:
    """
    A kernel caching mechanism to avoid recompilation.
    """
    _cache = {}

    @staticmethod
    def get_or_compile(kernel_source, options=None):
        """
        Retrieve a cached kernel or compile a new one if not cached.

        Args:
            kernel_source (str): The CUDA kernel source code as a string.
            options (list): Additional compiler options.

        Returns:
            KernelManager: A KernelManager object managing the compiled kernel.
        """
        key = hashlib.md5(kernel_source.encode()).hexdigest()
        if key not in KernelCache._cache:
            logger.info("Kernel not found in cache. Compiling new kernel.")
            kernel_manager = KernelManager(kernel_source)
            kernel_manager.compile(options)
            KernelCache._cache[key] = kernel_manager
        else:
            logger.info("Kernel found in cache. Reusing compiled kernel.")
        return KernelCache._cache[key]


# Utility function for kernel compilation
def compile_kernel(kernel_source, options=None):
    """
    Compile a CUDA kernel source code.

    This function attempts to compile the provided CUDA source code and return 
    a `KernelManager` instance that manages the compiled kernel.

    Args:
        kernel_source (str): The CUDA kernel source code.
        options (list, optional): Additional compiler options such as optimization flags.

    Returns:
        KernelManager: An instance of KernelManager managing the compiled kernel.

    Example:
        kernel_source = "kernel void add(int *a, int *b, int *c) { ... }"
        kernel_manager = compile_kernel(kernel_source, options=['--use_fast_math'])
        add_function = kernel_manager.get_function('add')
    """
    return KernelCache.get_or_compile(kernel_source, options)



def auto_tune_kernel(kernel_source, function_name, grid_sizes, block_sizes, test_func, options=None):
    """
    Auto-tune the kernel for optimal grid and block sizes.

    Args:
        kernel_source (str): The CUDA kernel source code.
        function_name (str): The name of the kernel function to optimize.
        grid_sizes (list): List of grid size tuples to test.
        block_sizes (list): List of block size tuples to test.
        test_func (callable): A function that runs the kernel and returns performance metrics.
        options (list): Additional compiler options.

    Returns:
        tuple: Optimal grid and block sizes.
    """
    kernel_manager = compile_kernel(kernel_source, options)
    kernel_function = kernel_manager.get_function(function_name)

    best_time = float('inf')
    best_config = None

    for grid in grid_sizes:
        for block in block_sizes:
            try:
                time = test_func(kernel_function, grid, block)
                logger.info(f"Tested grid={grid}, block={block}, time={time:.2f} ms")
                if time < best_time:
                    best_time = time
                    best_config = (grid, block)
            except Exception as e:
                logger.warning(f"Kernel execution failed for grid={grid}, block={block}: {e}")

    logger.info(f"Optimal configuration: grid={best_config[0]}, block={best_config[1]}, time={best_time:.2f} ms")
    return best_config
