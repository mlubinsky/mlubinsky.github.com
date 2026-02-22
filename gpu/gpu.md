## GPU

https://habr.com/ru/articles/996610/ От MNIST к Transformer. Hello CUDA.

https://habr.com/ru/articles/1001886/ От MNIST к Transformer. Часть 2. Основы работы с памятью

https://habr.com/ru/articles/994956/

https://habr.com/ru/articles/995170/

https://github.com/infatoshi/cuda-course

https://www.youtube.com/watch?v=86FAWCzIe_4

https://modal.com/gpu-glossary

https://jax-ml.github.io/scaling-book/

https://jamesakl.com/posts/cuda-ontology/

https://news.ycombinator.com/item?id=45947437

https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=high-level_overview

https://docs.nvidia.com/cuda/pdf/CUDA_C_Programming_Guide.pdf

https://docs.nvidia.com/cuda/pdf/CUDA_Runtime_API.pdf

https://www.bitsand.cloud/posts/profiling-gpus

https://leanpub.com/pythongpuprogramming Practical GPU Programming

https://damek.github.io/random/basic-facts-about-gpus/

https://enccs.github.io/gpu-programming/2-gpu-ecosystem/

https://habr.com/ru/companies/ruvds/articles/921024/ TPU from Google

https://stem-c.com/product/programming-massively-parallel-processors-a-hands-on-approach 

https://talkpython.fm/episodes/show/509/gpu-programming-in-pure-python

https://habr.com/ru/companies/timeweb/articles/909122/

https://news.ycombinator.com/item?id=44216123

https://thechipletter.substack.com/p/demystifying-gpu-compute-architectures

https://habr.com/ru/companies/selectel/articles/912108/

https://blog.codingconfessions.com/p/gpu-computing

https://www.youtube.com/watch?v=h9Z4oGN89MU

https://medium.com/@muhammedashraf2661/cuda-programming-an-introduction-to-gpu-architecture-dfd8dfffa13f

https://blog.codingconfessions.com/p/gpu-computing

https://github.com/srush/GPU-Puzzles

https://www.pyspur.dev/blog/introduction_cuda_programming

https://news.ycombinator.com/item?id=43121059

https://www.i-programmer.info/news/91-hardware/17763-demystifying-gpu-terminology.html

https://www.youtube.com/watch?v=v_q2JTIqE20

https://github.com/cuda-mode/lectures

https://arxiv.org/abs/2503.20481

https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html

https://thechipletter.substack.com/p/demystifying-gpu-compute-architectures

https://news.ycombinator.com/item?id=39279163

https://medium.com/@penberg/demystifying-gpus-for-cpu-centric-programmers-e24934a620f1

https://arxiv.org/pdf/2103.13937.pdf CUDA Tutorial

[https://www.youtube.com/watch?v=smlDvXVbyTo ](https://www.youtube.com/playlist?list=PL4_hYwCyhAvbhhT3F80vt1FdB2TqklRsM)

https://www.youtube.com/playlist?list=PL4_hYwCyhAvbhhT3F80vt1FdB2TqklRsM  RU


https://jax-ml.github.io/scaling-book/gpus/

https://news.ycombinator.com/item?id=44943666


Great news — your CUDA knowledge transfers well conceptually. Here's the lay of the land:

## Apple's Answer to CUDA: Metal

Apple Silicon GPUs (M1/M2/M3/M4 in Mac Studio) use **Metal** as the low-level GPU framework. There's no CUDA on Apple silicon — NVIDIA and Apple parted ways — so the stack looks like this:

| CUDA Concept | Apple Equivalent |
|---|---|
| CUDA C++ kernels | Metal Shading Language (MSL) — C++14-based |
| `__global__` kernels | `kernel` functions in MSL |
| cuBLAS / cuDNN | Metal Performance Shaders (MPS) |
| CUDA streams | Metal command queues / command buffers |
| Unified memory (newer CUDA) | Unified memory is *default* on Apple Silicon |
| nvcc | Xcode + Metal compiler (xcrun -sdk macosx metal) |
| Nsight | Xcode GPU Frame Capture / Instruments |

---

## Your Main Options

### 1. Metal (Native, lowest level)
Write compute kernels in **Metal Shading Language** — it looks very much like CUDA C++:

```metal
// CUDA: __global__ void add(float* a, float* b, float* c, int n)
kernel void add(device float* a [[buffer(0)]],
                device float* b [[buffer(1)]],
                device float* c [[buffer(2)]],
                uint idx [[thread_position_in_grid]]) {
    c[idx] = a[idx] + b[idx];
}
```

Host-side dispatch uses Objective-C or Swift via the Metal API (`MTLDevice`, `MTLCommandQueue`, etc.). You can also use **C++ with Metal-cpp** (Apple provides a header-only C++ wrapper).

### 2. Metal Performance Shaders (MPS)
Pre-built GPU primitives for ML/compute — analogous to cuBLAS+cuDNN. Great for matrix ops, convolutions, etc. without writing kernels manually.

### 3. MLX (Recommended for ML/Array work)
Apple's own **NumPy/JAX-like framework** for Apple Silicon, open-sourced in late 2023. If you're doing ML or numerical work, this is the fastest path:
```python
import mlx.core as mx
a = mx.array([1.0, 2.0, 3.0])
b = a * 2  # runs on GPU lazily
mx.eval(b)
```
It has automatic differentiation and feels like PyTorch/JAX.

### 4. PyTorch with MPS backend
PyTorch supports Apple GPU via the MPS backend — easiest migration if you already have CUDA PyTorch code:
```python
device = torch.device("mps")
tensor = torch.randn(1000, 1000).to(device)
```
Most ops work; some less common ops fall back to CPU.

### 5. OpenCL (avoid)
Deprecated by Apple in macOS 10.14. Don't bother.

---

## Key Differences to Know Coming from CUDA

- **No warp concept** — Apple GPUs use SIMD groups (typically 32 wide, similar to warps but called `simdgroup`)
- **Unified memory is always on** — no explicit `cudaMemcpy` needed; CPU and GPU share the same physical memory
- **No `__shared__` exactly** — use `threadgroup` memory instead (same idea, different keyword)
- **Threadgroup = CUDA block**, `thread_position_in_grid` = global thread index
- **No dynamic parallelism** in Metal (can't launch kernels from kernels)

---

## Recommended Path

If you're doing **ML/data work** → start with **PyTorch MPS** or **MLX**  
If you want **custom kernels** → learn **Metal compute shaders** (your CUDA knowledge maps almost directly)  
If you want the **best performance** → Metal + MPS together

The [Apple Metal documentation](https://developer.apple.com/documentation/metal) and the [MLX GitHub](https://github.com/ml-explore/mlx) are both excellent starting points.
