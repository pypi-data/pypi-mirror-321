# CUDA Utilities with PyCUDA

This project provides a collection of utilities and abstractions to simplify the use of **PyCUDA** for managing CUDA kernels, GPU memory, profiling, and more. These tools are designed to help developers write efficient and reusable GPU-accelerated Python applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Kernel Compilation](#kernel-compilation)
  - [GPU Memory Management](#gpu-memory-management)
  - [Profiling](#profiling)
  - [Utility Functions](#utility-functions)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Kernel Compilation and Caching**: Compile and cache CUDA kernels to optimize performance.
- **GPU Memory Management**: High-level abstractions for allocating, copying, and managing GPU memory.
- **Profiling**: Utilities for timing CUDA kernel executions and other Python functions.
- **Utility Functions**: Random array generation, array comparison, reshaping, and summary statistics.

## Installation

Ensure you have **PyCUDA** installed. If not, you can install it via pip:

```bash
pip install -r requirements.txt
```

Clone the repository:

```bash
git clone https://github.com/takuphilchan/pycuda_plus.git
cd pycuda_plus
```

## Usage

### Kernel Compilation

The `KernelManager` and `KernelCache` classes simplify the process of compiling and managing CUDA kernels.

#### Example:

```python
from pycuda_plus.kernel import compile_kernel

kernel_source = """__global__ void add(float *a, float *b, float *c) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    c[idx] = a[idx] + b[idx];
}"""

kernel_manager = compile_kernel(kernel_source)
add_function = kernel_manager.get_function("add")
```

### GPU Memory Management

The `GPUArray` class provides an abstraction for GPU memory, while the `GPUMemoryPool` manages pooled allocations.

#### Example:

```python
from pycuda_plus.memory import allocate
import numpy as np

# Allocate GPU memory
shape = (1024,)
gpu_array = allocate(shape)

# Copy data to GPU
host_array = np.random.rand(*shape).astype(np.float32)
gpu_array.copy_to_device(host_array)

# Copy data back to host
result = gpu_array.copy_to_host()
```

### Profiling

The `Profiler` class helps measure the execution time of CUDA kernels and Python functions.

#### Example:

```python
from pycuda_plus.profiler import Profiler

execution_time = Profiler.time_kernel(
    kernel_function=add_function,
    grid=(32, 1, 1),
    block=(32, 1, 1),
    a_gpu, b_gpu, c_gpu
)
print(f"Kernel execution time: {execution_time} ms")
```

### Utility Functions

#### Generate Random Arrays:

```python
from utils import generate_random_array

random_array = generate_random_array(shape=(1024,), min_val=0.0, max_val=1.0)
```

#### Compare Arrays:

```python
from pycuda_plus.utils import compare_arrays

compare_arrays(array1, array2, atol=1e-5)
```

#### Print Array Summary:

```python
from pycuda_plus.utils import print_array_summary

print_array_summary(array)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore and extend the functionality as needed!

