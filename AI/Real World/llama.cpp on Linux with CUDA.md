---
tags: [ai, ai/realworld, linux]
title: llama.cpp compilation with CUDA (Linux)
date created: Wednesday, July 16th 2025, 11:32:27 am
date modified: Friday, July 10th 2026, 10:40:13 am
parent: Real World
nav_order: 4
---
# `llama.cpp` compilation with CUDA (Linux)
**For more detailed guides check [`llama.cpp`'s official build guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)**

> [!IMPORTANT] Prerequisites
> Install [`cuda-tookit`](https://developer.nvidia.com/cuda-downloads)[^1], `cmake`, `git` before proceeding

## Compilation
First `git clone` the repository

```bash
$ git clone https://github.com/ggml-org/llama.cpp.git
$ cd llama.cpp
```

Then:

```bash
$ cmake -B build -DGGML_CUDA=ON
  cmake --build build --config Release
```

> [!IMPORTANT]
> If `CUDACXX` or `CMAKE_CUDA_COMPILER` is wrong (no `nvcc` CUDA compiler) add `-DCMAKE_CUDA_COMPILER=cuda/toolkit/path` (probably will be in `/usr/local/cuda-VERSION/bin/nvcc`) and `-DCUDAToolkit_ROOT=cuda/toolkit/root/path` (probably will be `/usr/local/cuda-VERSION`)

> If they tell you `ccache` is not found add `-DGGML_CACHE=OFF`

> On `cmake --build build --config Release`, if `nvcc` spews out a warning saying `no gpu found`, then redo the first step and add `-DCMAKE_CUDA_ARCHITECTURES="COMPUTE_LEVELS_OF_YOUR_SYSTEM"` (e.g. you only have compute level `8.6` devices do: `-DCMAKE_CUDA_ARCHITECTURES="86"`, add `;` to separate difference compute levels, i.e. `86;89`)

> If `cmake` says OpenSSL is not found try installing `libssl-dev` (the shared libraries for OpenSSL)

> You may need to restart as well.

## Optional Nice-to-haves
- Installing `nvtop`
- Creating a symlink to the `./llama.cpp/build/bin` folder and the `llama.cpp` models folder (on Linux: `~/.cache/llama.cpp/`; MacOS `~/Libray/Caches/llama.cpp` )
- Creating an alias to updating `llama.cpp` (maybe also setup a `cron` job for that matter)
- Capping the power limit to prevent spikes that cause the PSU to turn off the system (w/ `nvidia-smi -i [GPU (0/1/2/etc)] -pl (POWER LIMIT IN WATTS))
- Set `LLAMA_ARG_LOG_FILE` to have logs in a file (not just `stdout`)

[^1]: At least on Ubuntu you can just do `sudo apt install nvidia-cuda-toolkit`, it's easier to install and manage as it's installed from `apt`[^2]
[^2]: If you decide to follow the Nvidia instructions, it is obviously more official, and if you find it annoying to only install one specified version, you can just install w/ something like this: `sudo apt-get -y install cuda` (just saying `cuda` just installs everything)

#ai #ai/realworld #linux 
