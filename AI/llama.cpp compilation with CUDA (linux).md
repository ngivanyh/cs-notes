Install [`cuda-tookit`](https://developer.nvidia.com/cuda-downloads), `cmake`

```bash
$ git clone https://github.com/ggml-org/llama.cpp.git
$ cd llama.cpp
```

Try:
```bash
$ cmake -B build -DGGML_CUDA=ON
  cmake --build build --config Release
```

If `CUDACXX` or `CMAKE_CUDA_COMPILER` is wrong (no `nvcc` CUDA compiler) add `-DCMAKE_CUDA_COMPILER=cuda/toolkit/path` (probably will be in `/usr/local/cuda-VER/bin/nvcc`) and `-DCUDAToolkit_ROOT=cuda/toolkit/root/path` (probably will be `/usr/local/cuda-VER`)

If they tell you `ccache` is not found add `-DGGML_CACHE=OFF`

On `cmake --build build --config Release`, if `nvcc` spews out a warning saying `no gpu found`, then redo the first step and add `-DCMAKE_CUDA_ARCHITECTURES="COMPUTE_LEVELS_OF_YOUR_SYSTEM"` (e.g. you only have compute level `8.6` devices do: `-DCMAKE_CUDA_ARCHITECTURES="86"`, add `;` to separate difference compute levels, i.e. `86;89`)

You may need to restart as well.

#ai #ai/inference #llama-cpp