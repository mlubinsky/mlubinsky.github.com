https://github.com/google-ai-edge/LiteRT/tree/main/tflite/examples/minimal
```
root@spotace:~/MICHAEL/TF# cd minimal_build

root@spotace:~/MICHAEL/TF/minimal_build# cmake ../tensorflow/tensorflow/lite/examples/minimal
-- The C compiler identification is GNU 9.4.0
-- The CXX compiler identification is GNU 9.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to Release, for debug builds use'-DCMAKE_BUILD_TYPE=Debug'.
CMake Warning at /root/MICHAEL/TF/minimal_build/abseil-cpp/CMakeLists.txt:77 (message):
  A future Abseil release will default ABSL_PROPAGATE_CXX_STD to ON for CMake
  3.8 and up.  We recommend enabling this option to ensure your project still
  builds correctly.


-- Performing Test ABSL_INTERNAL_AT_LEAST_CXX17
-- Performing Test ABSL_INTERNAL_AT_LEAST_CXX17 - Success
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
--
-- Configured Eigen 3.4.90
--
-- Performing Test FARMHASH_HAS_BUILTIN_EXPECT
-- Performing Test FARMHASH_HAS_BUILTIN_EXPECT - Success
-- Proceeding with version: 24.3.25.4
-- Looking for strtof_l
-- Looking for strtof_l - found
-- Looking for strtoull_l
-- Looking for strtoull_l - found
-- Looking for realpath
-- Looking for realpath - found
-- CMAKE_CXX_FLAGS:
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Downloading pthreadpool to /root/MICHAEL/TF/minimal_build/pthreadpool-source (define SYSTEM_PTHREADPOOL or PTHREADPOOL_SOURCE_DIR to avoid it)
-- Configuring done
-- Generating done
-- Build files have been written to: /root/MICHAEL/TF/minimal_build/pthreadpool-download
Scanning dependencies of target pthreadpool
[ 11%] Creating directories for 'pthreadpool'
[ 22%] Performing download step (download, verify and extract) for 'pthreadpool'
-- Downloading...
   dst='/root/MICHAEL/TF/minimal_build/pthreadpool-download/pthreadpool-prefix/src/4fe0e1e183925bf8cfa6aae24237e724a96479b8.zip'
   timeout='none'
-- Using src='https://github.com/Maratyszcza/pthreadpool/archive/4fe0e1e183925bf8cfa6aae24237e724a96479b8.zip'
-- verifying file...
       file='/root/MICHAEL/TF/minimal_build/pthreadpool-download/pthreadpool-prefix/src/4fe0e1e183925bf8cfa6aae24237e724a96479b8.zip'
-- Downloading... done
-- extracting...
     src='/root/MICHAEL/TF/minimal_build/pthreadpool-download/pthreadpool-prefix/src/4fe0e1e183925bf8cfa6aae24237e724a96479b8.zip'
     dst='/root/MICHAEL/TF/minimal_build/pthreadpool-source'
-- extracting... [tar xfz]
-- extracting... [analysis]
-- extracting... [rename]
-- extracting... [clean up]
-- extracting... done
[ 33%] No patch step for 'pthreadpool'
[ 44%] No update step for 'pthreadpool'
[ 55%] No configure step for 'pthreadpool'
[ 66%] No build step for 'pthreadpool'
[ 77%] No install step for 'pthreadpool'
[ 88%] No test step for 'pthreadpool'
[100%] Completed 'pthreadpool'
[100%] Built target pthreadpool
-- Downloading FXdiv to /root/MICHAEL/TF/minimal_build/FXdiv-source (define FXDIV_SOURCE_DIR to avoid it)
-- Configuring done
-- Generating done
-- Build files have been written to: /root/MICHAEL/TF/minimal_build/FXdiv-download
Scanning dependencies of target fxdiv
[ 11%] Creating directories for 'fxdiv'
[ 22%] Performing download step (git clone) for 'fxdiv'
Cloning into 'FXdiv-source'...
Already on 'master'
Your branch is up to date with 'origin/master'.
[ 33%] No patch step for 'fxdiv'
[ 44%] Performing update step for 'fxdiv'
Current branch master is up to date.
[ 55%] No configure step for 'fxdiv'
[ 66%] No build step for 'fxdiv'
[ 77%] No install step for 'fxdiv'
[ 88%] No test step for 'fxdiv'
[100%] Completed 'fxdiv'
[100%] Built target fxdiv
-- Downloading FP16 to /root/MICHAEL/TF/minimal_build/FP16-source (define FP16_SOURCE_DIR to avoid it)
-- Configuring done
-- Generating done
-- Build files have been written to: /root/MICHAEL/TF/minimal_build/FP16-download
Scanning dependencies of target fp16
[ 11%] Creating directories for 'fp16'
[ 22%] Performing download step (download, verify and extract) for 'fp16'
-- Downloading...
   dst='/root/MICHAEL/TF/minimal_build/FP16-download/fp16-prefix/src/0a92994d729ff76a58f692d3028ca1b64b145d91.zip'
   timeout='none'
-- Using src='https://github.com/Maratyszcza/FP16/archive/0a92994d729ff76a58f692d3028ca1b64b145d91.zip'
-- [download 1% complete]
-- [download 14% complete]
-- [download 44% complete]
-- [download 93% complete]
-- [download 100% complete]
-- verifying file...
       file='/root/MICHAEL/TF/minimal_build/FP16-download/fp16-prefix/src/0a92994d729ff76a58f692d3028ca1b64b145d91.zip'
-- Downloading... done
-- extracting...
     src='/root/MICHAEL/TF/minimal_build/FP16-download/fp16-prefix/src/0a92994d729ff76a58f692d3028ca1b64b145d91.zip'
     dst='/root/MICHAEL/TF/minimal_build/FP16-source'
-- extracting... [tar xfz]
-- extracting... [analysis]
-- extracting... [rename]
-- extracting... [clean up]
-- extracting... done
[ 33%] No patch step for 'fp16'
[ 44%] No update step for 'fp16'
[ 55%] No configure step for 'fp16'
[ 66%] No build step for 'fp16'
[ 77%] No install step for 'fp16'
[ 88%] No test step for 'fp16'
[100%] Completed 'fp16'
[100%] Built target fp16
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Building for XNNPACK_TARGET_PROCESSOR: x86_64
-- Found Python: /usr/local/bin/python3 (found version "3.11.11") found components: Interpreter
-- Generating microkernels.cmake
No microkernel found in src/reference/packing.cc
No microkernel found in src/reference/unary-elementwise.cc
No microkernel found in src/reference/binary-elementwise.cc
--
-- 3.21.9.0
-- Performing Test protobuf_HAVE_LD_VERSION_SCRIPT
-- Performing Test protobuf_HAVE_LD_VERSION_SCRIPT - Success
-- Performing Test protobuf_HAVE_BUILTIN_ATOMICS
-- Performing Test protobuf_HAVE_BUILTIN_ATOMICS - Success
-- Configuring done
-- Generating done
-- Build files have been written to: /root/MICHAEL/TF/minimal_build
```
