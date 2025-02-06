<https://builtin.com/machine-learning/introduction-deep-learning-tensorflow-20>

<https://habr.com/ru/post/500788/>


### LiteRT

The TensorFlow framework provides tools and APIs to convert a standard pretrained TensorFlow model from the SavedModel or Keras format into a LiteRT format.

https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-54/tensorflow-lite-developer-workflow.html

https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-54/sample-applications.html

https://github.com/tensorflow/tensorflow/tree/v2.16.1/tensorflow/lite

https://github.com/tensorflow/tflite-support

https://www.kaggle.com/models?framework=tfLite



### XNNPACK
https://github.com/google/XNNPACK

https://developers.googleblog.com/en/streamlining-llm-inference-at-the-edge-with-tflite

https://onnxruntime.ai/docs/execution-providers/Xnnpack-ExecutionProvider.html
```
XNNPACK is a highly optimized solution for neural network inference on ARM, x86, WebAssembly, and RISC-V platforms.
 XNNPACK is not intended for direct use by deep learning practitioners and researchers;
instead it provides low-level performance primitives for accelerating high-level machine learning frameworks,
such as TensorFlow Lite, TensorFlow.js, PyTorch, ONNX Runtime, and MediaPipe.

```

### TensorFlow Lite C++ image classification demo
https://github.com/google-ai-edge/LiteRT/tree/main/tflite/examples/label_image

root@spotace:~/MICHAEL/LiteRT# bazel build -c opt //tflite/examples/label_image:label_image

```
INFO: Found 1 target...
ERROR: /root/.cache/bazel/_bazel_root/f52f4cfffd1f0610b8c20da624b0b2f6/external/XNNPACK/BUILD.bazel:670:36: Compiling src/f16-vbinary/gen/f16-vsubc-avx512fp16-u64.c failed: (Exit 1):
gcc failed: error executing command (from target @XNNPACK//:avx512fp16_prod_microkernels)
/usr/bin/gcc -U_FORTIFY_SOURCE -fstack-protector -Wall -Wunused-but-set-parameter -Wno-free-nonheap-object -fno-omit-frame-pointer -g0 -O2 '-D_FORTIFY_SOURCE=1' -DNDEBUG -ffunction-sections ... (remaining 120 arguments skipped)
gcc: error: unrecognized command line option '-mavx512fp16'; did you mean '-mavx512f'?
Target //tflite/examples/label_image:label_image failed to build
Use --verbose_failures to see the command lines of failed build steps.
INFO: Elapsed time: 41.675s, Critical Path: 18.71s
INFO: 163 processes: 9 internal, 154 local.
FAILED: Build did NOT complete successfully


This error occurs because your version of GCC does not support the -mavx512fp16 option.
This flag enables AVX-512 FP16 (16-bit floating point) instructions,
which were introduced in Intel's Sapphire Rapids processors and are only supported in GCC 12+.

The suggestion "-mavx512f" refers to the base AVX-512 feature set,
 which is supported by earlier processors and compilers.


2. Upgrade GCC (If Needed)
On macOS (Homebrew):
-------------------
brew upgrade gcc

On Ubuntu/Debian:
------------------
sudo apt update
sudo apt install gcc-12 g++-12
Then, use gcc-12 explicitly:

 
3. Use a Compatible Flag
If you cannot upgrade GCC, replace -mavx512fp16 with -mavx512f, which is supported in older GCC versions:


gcc my_program.c -o my_program -mavx512f

However, this will disable FP16 support. If your code depends on FP16 operations, you must upgrade to GCC 12+.
```

### bazel test
```
cd ~/MICHAEL/LiteRT
bazel test  --define xnn_enable_avxvnni=false --define xnn_enable_avx512amx=false  --define xnn_enable_avx512fp16=false   --define xnn_enable_avxvnniint8=false  //tflite:interpreter_test

```
### Install CMake
```
1. Check Current Version

cmake --version
Your output shows 3.16.3, which is an older version.

2. Remove Old CMake (Optional)
If you installed CMake using apt, remove it first:

sudo apt remove --purge cmake
This ensures no conflicts with the newer version.

3. Install CMake 3.31.5 from Official Binary (Recommended)
Since Ubuntu’s repositories often do not include the latest CMake versions, it’s best to download the official release.

Download CMake 3.31.5 (Precompiled Binary)

wget https://github.com/Kitware/CMake/releases/download/v3.31.5/cmake-3.31.5-linux-x86_64.sh

Make the Script Executable

chmod +x cmake-3.31.5-linux-x86_64.sh
Run the Installer

sudo ./cmake-3.31.5-linux-x86_64.sh --prefix=/opt/cmake --skip-license
This installs CMake into /opt/cmake.

Update PATH Add CMake to your system’s PATH:

echo 'export PATH=/opt/cmake/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

Verify Installation: 
cmake --version


Alternative: Build CMake from Source
--------------------------------
If you prefer to build from source:

Install Dependencies

sudo apt update
sudo apt install -y build-essential libssl-dev
Download Source Code

 
wget https://github.com/Kitware/CMake/releases/download/v3.31.5/cmake-3.31.5.tar.gz
tar -xvzf cmake-3.31.5.tar.gz
cd cmake-3.31.5
Compile and Install

./bootstrap
make -j$(nproc)
sudo make install
Verify Installation

cmake --version

```

### Build LiteRT with CMake

cmake --version  
cmake version 3.16.3  

https://ai.google.dev/edge/litert/build/cmake  
```
git clone https://github.com/tensorflow/tensorflow.git 
mkdir tflite_build  
cd tflite_build  
cmake ../tensorflow/tensorflow/lite  
```

### Android 

https://developer.android.com/ndk

The recommended Android NDK version for building LiteRT is 25b. This can be found here: https://ai.google.dev/edge/litert/android/lite_build

https://dl.google.com/android/repository/android-ndk-r27c-linux.zip

Suggested here: https://ai.google.dev/edge/litert/build/cmake
to build TFLite for Android :
```
cat ./android.sh

cmake -DCMAKE_TOOLCHAIN_FILE=/root/MICHAEL/NDK/android-ndk-r27c/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a   /root/MICHAEL/TF/tensorflow/tensorflow/lite/

root@spotace:~/MICHAEL# ./android.sh

ERROR:
CMake Error at CMakeLists.txt:83 (message):
  When cross-compiling, some tools need to be available to run on the host
  (current required tools: flatc).  Please specify where those binaries can
  be found by using -DTFLITE_HOST_TOOLS_DIR=<flatc_dir_path>.


root@spotace:~/MICHAEL/TF/flatc-native-build# ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  compile_commands.json  _deps  flatbuffers  flatbuffers-flatc  Makefile

cmake -DCMAKE_TOOLCHAIN_FILE=/root/MICHAEL/NDK/android-ndk-r27c/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a  -DTFLITE_HOST_TOOLS_DIR=/root/MICHAEL/TF/flatc-native-build/flatbuffers  /root/MICHAEL/TF/tensorflow/tensorflow/lite/
                                                   /root/MICHAEL/TF/flatc-native-build/flatbuffers-flatc/bin/

CMake Error at CMakeLists.txt:94 (message):
  Host 'flatc' compiler has not been found in the following locations:
  /root/MICHAEL/TF/flatc-native-build/flatbuffers;/root/MICHAEL/TF/flatc-native-build/flatbuffers/bin;/root/MICHAEL/TF/flatc-native-build/flatbuffers/flatbuffers-flatc/bin



```

### Cross-compilation
```
You can use CMake to build binaries for ARM64 or Android target architectures.

In order to cross-compile the LiteRT, you namely need to provide the path to the SDK
(e.g. ARM64 SDK or NDK in Android's case) with -DCMAKE_TOOLCHAIN_FILE flag.

cmake -DCMAKE_TOOLCHAIN_FILE=<CMakeToolchainFileLoc> ../tensorflow/lite/
```

#### Specifics of Android cross-compilation
```
For Android cross-compilation, you need to install Android NDK and provide the NDK path
with -DCMAKE_TOOLCHAIN_FILE flag mentioned above.

You also need to set target ABI with-DANDROID_ABI flag.

cmake -DCMAKE_TOOLCHAIN_FILE=<NDK path>/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a ../tensorflow_src/tensorflow/lite
```
#### Specifics of kernel (unit) tests cross-compilation
```
Cross-compilation of the unit tests requires flatc compiler for the host architecture.
For this purpose, there is a CMakeLists located in tensorflow/lite/tools/cmake/native_tools/flatbuffers
to build the flatc compiler with CMake in advance in a separate build directory using the host toolchain.

mkdir flatc-native-build && cd flatc-native-build
cmake ../tensorflow_src/tensorflow/lite/tools/cmake/native_tools/flatbuffers

root@spotace:~/MICHAEL/TF# mkdir flatc-native-build && cd flatc-native-build
root@spotace:~/MICHAEL/TF/flatc-native-build# cmake ../tensorflow/tensorflow/lite/tools/cmake/native_tools/flatbuffers
-- The C compiler identification is GNU 9.4.0
-- The CXX compiler identification is GNU 9.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning (dev) at /opt/cmake/share/cmake-3.31/Modules/FetchContent.cmake:1953 (message):
  Calling FetchContent_Populate(flatbuffers) is deprecated, call
  FetchContent_MakeAvailable(flatbuffers) instead.  Policy CMP0169 can be set
  to OLD to allow FetchContent_Populate(flatbuffers) to be called directly
  for now, but the ability to call it with declared details will be removed
  completely in a future version.
Call Stack (most recent call first):
  /root/MICHAEL/TF/tensorflow/tensorflow/lite/tools/cmake/modules/OverridableFetchContent.cmake:537 (FetchContent_Populate)
  /root/MICHAEL/TF/tensorflow/tensorflow/lite/tools/cmake/modules/flatbuffers.cmake:35 (OverridableFetchContent_Populate)
  /root/MICHAEL/TF/tensorflow/tensorflow/lite/tools/cmake/modules/FindFlatBuffers.cmake:18 (include)
  CMakeLists.txt:43 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Proceeding with version: 24.3.25.4
-- Looking for strtof_l
-- Looking for strtof_l - found
-- Looking for strtoull_l
-- Looking for strtoull_l - found
-- Looking for realpath
-- Looking for realpath - found
-- CMAKE_CXX_FLAGS:
-- Configuring done (3.7s)
-- Generating done (0.0s)
-- Build files have been written to: /root/MICHAEL/TF/flatc-native-build



cmake --build .
It is also possible to install the flatc to a custom installation location
(e.g. to a directory containing other natively-built tools instead of the CMake build directory):


cmake -DCMAKE_INSTALL_PREFIX=<native_tools_dir> ../tensorflow_src/tensorflow/lite/tools/cmake/native_tools/flatbuffers
cmake --build .

For the LiteRT cross-compilation itself, additional parameter
 -DTFLITE_HOST_TOOLS_DIR=<flatc_dir_path> pointing to the directory containing
 the native flatc binary needs to be provided along with the -DTFLITE_KERNEL_TEST=on flag mentioned above.


cmake -DCMAKE_TOOLCHAIN_FILE=${OE_CMAKE_TOOLCHAIN_FILE} -DTFLITE_KERNEL_TEST=on -DTFLITE_HOST_TOOLS_DIR=<flatc_dir_path> ../tensorflow/lite/
```

### Cross-compiled kernel (unit) tests launch on target
```
Unit tests can be run as separate executables or using the CTest utility.
As far as CTest is concerned,
if at least one of the parameters TFLITE_ENABLE_XNNPACKorTFLITE_EXTERNAL_DELEGATE` is enabled for the

LiteRT build, the resulting tests are generated with two different labels (utilizing the same test executable):
- plain - denoting the tests ones run on CPU backend
- delegate - denoting the tests expecting additional launch arguments used for the used delegate specification

Both CTestTestfile.cmake and run-tests.cmake (as referred below) are available in <build_dir>/kernels.

Launch of unit tests with CPU backend (provided the CTestTestfile.cmake is present on target in the current directory):


ctest -L plain
Launch examples of unit tests using delegates (provided the CTestTestfile.cmake
as well as run-tests.cmake file are present on target in the current directory):


cmake -E env TESTS_ARGUMENTS=--use_xnnpack=true ctest -L delegate
cmake -E env TESTS_ARGUMENTS=--external_delegate_path=<PATH> ctest -L delegate

A known limitation of this way of providing additional delegate-related launch arguments to unit tests is
that it effectively supports only those with an expected return value of 0.
Different return values will be reported as a test failure.

find . -name CMakeLists.txt
./tflite/kernels/CMakeLists.txt
./tflite/tools/benchmark/CMakeLists.txt
./tflite/tools/cmake/native_tools/flatbuffers/CMakeLists.txt
./tflite/tools/cmake/modules/farmhash/CMakeLists.txt
./tflite/tools/cmake/modules/xnnpack/CMakeLists.txt
./tflite/tools/cmake/modules/fft2d/CMakeLists.txt
./tflite/tools/cmake/modules/ml_dtypes/CMakeLists.txt
./tflite/CMakeLists.txt
./tflite/profiling/proto/CMakeLists.txt
./tflite/examples/minimal/CMakeLists.txt
./tflite/examples/label_image/CMakeLists.txt
./tflite/c/CMakeLists.txt
./third_party/tensorflow/third_party/xla/xla/mlir_hlo/mhlo/CMakeLists.txt
./third_party/tensorflow/third_party/xla/xla/mlir_hlo/mhlo/analysis/CMakeLists.txt
./third_party/tensorflow/third_party/xla/xla/mlir_hlo/mhlo/IR/CMakeLists.txt
...
...
./third_party/tensorflow/tensorflow/lite/CMakeLists.txt
./third_party/tensorflow/tensorflow/lite/profiling/proto/CMakeLists.txt
./third_party/tensorflow/tensorflow/lite/examples/minimal/CMakeLists.txt
./third_party/tensorflow/tensorflow/lite/examples/label_image/CMakeLists.txt
./third_party/tensorflow/tensorflow/lite/c/CMakeLists.txt

```

### CMake for Ubuntu

```
Method 1: Install from Ubuntu Repositories (Easy but May Be Outdated)
 
sudo apt update
sudo apt install cmake -y
After installation, check the version:

 
cmake --version
If you need a newer version, use Method 2.

Method 2: Install Latest CMake from Kitware APT Repository
Kitware provides the latest CMake versions officially.

Add the Kitware APT Repository:

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update

Install the latest CMake:

sudo apt install cmake -y

Method 3: Install Latest CMake from Source (Most Up-to-Date)
Remove old CMake (if installed):

sudo apt remove cmake -y
Download the latest CMake:

wget https://github.com/Kitware/CMake/releases/latest/download/cmake-linux-x86_64.sh
Install it:

sudo bash cmake-linux-x86_64.sh --prefix=/usr/local --skip-license

Verify the installation:

cmake --version

Input for the CMake Build Tool
CMake takes CMakeLists.txt as its main input file.
This file defines how the project should be configured, built, and installed.

Common Inputs for CMake:
CMakeLists.txt (Main Input)

This file is placed in the root of the project and contains build instructions.
Example content:


cmake_minimum_required(VERSION 3.10)
project(MyProject)

add_executable(my_program main.cpp)
Source Files (e.g., .cpp, .c, .h)

CMake processes these source files based on the instructions in CMakeLists.txt.
Configuration Options (Passed via CLI or -D flags)

Example: Specify the build type:

cmake -DCMAKE_BUILD_TYPE=Release ..
Toolchain Files (For cross-compilation)

Example: toolchain.cmake for compiling on ARM.
Additional CMake Modules (e.g., FindPackage.cmake)

Used for finding dependencies like OpenCV, Boost, etc.
How CMake Uses These Inputs
Configure the Build System

Run CMake in the project directory:

cmake -S . -B build
This reads CMakeLists.txt and generates build files (like Makefile or ninja.build).
Build the Project

Once configured, compile the project:

cmake --build build

```


### Explanation of bazel test //tflite:interpreter_test
```
rm -rf  ~/.cache/bazel

bazel test  //tflite:interpreter_test
is used to run tests using Bazel. Let's break down its arguments:

bazel test

This is the Bazel command for running tests instead of just building targets.
It ensures that test rules specified in the BUILD files are executed.
 
This is the Bazel target you are running the test for.
//tflite refers to the tflite package, which is located in the tflite/ directory of the workspace.
interpreter_test is the test rule defined in the BUILD file inside tflite/.
In Bazel, the notation //tflite:interpreter_test refers to a target within a Bazel workspace.

Breakdown of //tflite:interpreter_test:
// → The root of the Bazel workspace.
tflite → A subdirectory (or package) within the repository.
interpreter_test → The target name, which is likely a test executable defined in a BUILD file.

Where is the test file located?
To find the actual test file check the tflite/ directory
Since the target is //tflite:interpreter_test, the corresponding BUILD file should be in:

LiteRT/tflite/BUILD

This file will define how interpreter_test is built and which source files it includes.

```
https://github.com/google-ai-edge/LiteRT/blob/main/tflite/BUILD
```
# Test main interpreter
cc_test(
    name = "interpreter_test",
    size = "small",
    srcs = [
        "interpreter_test.cc",
    ],
    features = ["-dynamic_link_test_srcs"],  # see go/dynamic_link_test_srcs
    tags = [
        "tflite_smoke_test",
    ],
...

Typically, the test file will be a .cc or .cpp file inside tflite/ with interpreter_test in its name.
Try searching for files like:
 
LiteRT/tflite/interpreter_test.cc
LiteRT/tflite/interpreter_test.cpp

find tflite -name "interpreter_test*"

Or, if using GitHub, check the tflite directory for relevant files.
```
https://github.com/google-ai-edge/LiteRT/tree/main/tflite



### LiteRT uses Bazel 6.5.0
```

sudo apt install bazel-6.5.0

https://github.com/bazelbuild/bazel/releases

https://github.com/bazelbuild/bazel/releases/download/6.5.0/bazel-6.5.0-installer-darwin-x86_64.sh

Run the installer:

chmod +x bazel-6.5.0-installer-darwin-x86_64.sh
./bazel-6.5.0-installer-darwin-x86_64.sh --user

Add Bazel to your PATH:

export PATH="$HOME/bin:$PATH"

Verify the version:

bazel --version

2. Use Bazelisk (Recommended)
--------------------------------
Bazelisk is a tool that automatically downloads and runs the appropriate version of Bazel for your project.
It respects the .bazelversion file in your repository.

Install Bazelisk using Homebrew:

brew install bazelisk
Create a .bazelversion file in your repository with the desired version:

echo "6.5.0" > .bazelversion
Run Bazel commands as usual:

bazelisk build //...
Bazelisk will automatically download and use Bazel 6.5.0.

3. Use Homebrew for Available Versions
---------------------------------------
Homebrew provides formulas for some older Bazel versions,
but these are typically named bazel@<major_version> (e.g., bazel@5).
To see which versions are available:

brew search bazel
If version 6.x is available, install it:

brew install bazel@6

4. Manually Build Bazel from Source
--------------------------------------
If the above options don’t work, you can build Bazel 6.5.0 from source:

Clone the Bazel repository:

git clone https://github.com/bazelbuild/bazel.git
cd bazel
git checkout 6.5.0

Build Bazel:

bash compile.sh
Use the generated bazel binary:

./output/bazel --version
```

## TFLite   LiteRT

Normally, you do not need to locally build LiteRT Android library.

https://ai.google.dev/edge/litert

https://github.com/google-ai-edge/LiteRT

https://github.com/google-ai-edge/litert-samples/tree/main/examples


git clone https://github.com/google-ai-edge/LiteRT
```
cd ci
/run_bazel_build.sh

ERROR: The project you're trying to build requires Bazel 6.5.0
 (specified in /Users/mlubinsky/CODE/LiteRT_2/LiteRT/.bazelversion),
but it wasn't found in
/opt/homebrew/Cellar/bazel/7.4.1/libexec/bin.

Bazel binaries for all official releases can be downloaded from here:
  https://github.com/bazelbuild/bazel/releases


You can download the required version directly using this command:
  (cd "/opt/homebrew/Cellar/bazel/7.4.1/libexec/bin" && curl -fLO https://releases.bazel.build/6.5.0/release/bazel-6.5.0-darwin-arm64 && chmod +x bazel-6.5.0-darwin-arm64)

I tried:

cat .bazelversion
6.5.0
 

/run_bazel_build.sh

(13:23:10) WARNING: --enable_bzlmod is set, but no MODULE.bazel file was found at the workspace root.
Bazel will create an empty MODULE.bazel file. Please consider migrating your external dependencies from WORKSPACE to MODULE.bazel.
For more details, please refer to https://github.com/bazelbuild/bazel/issues/18958.

(13:23:12) ERROR: /Users/mlubinsky/CODE/LiteRT_2/LiteRT/WORKSPACE:15:17: fetching local_repository rule //external:org_tensorflow: java.io.IOException: No MODULE.bazel, REPO.bazel, or WORKSPACE file found in
/Users/mlubinsky/CODE/LiteRT_2/LiteRT/third_party/tensorflow

(13:23:12) ERROR: Error computing the main repository mapping: no such package '@@org_tensorflow//tensorflow':
No MODULE.bazel, REPO.bazel, or WORKSPACE file found in
/Users/mlubinsky/CODE/LiteRT_2/LiteRT/third_party/tensorflow

https://github.com/google-ai-edge/LiteRT/blob/main/.gitmodules

[submodule "third_party/tensorflow"]
	path = third_party/tensorflow
	url = https://github.com/tensorflow/tensorflow
	branch = master


 Check for Submodules in the Repository
The repository may use git submodules for external dependencies like TensorFlow. Run the following commands to confirm and fetch missing submodules:

 
# Check for submodule configuration
cat .gitmodules
If third_party/tensorflow is listed in the .gitmodules file, it is a submodule.

2. Clone the Repository with Submodules
If you didn’t clone the repository with submodules initially, you can fix it like this:

 
# Initialize and fetch all submodules
git submodule update --init --recursive
If you need to re-clone the repository, use this command to include submodules from the start:
 
git clone --recurse-submodules https://github.com/google-ai-edge/LiteRT.git

LiteRT, formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.
The project's source code is available on GitHub:

https://github.com/google-ai-edge/LiteRT

cd /Users/mlubinsky/CODE/LiteRT_2/LiteRT/ci
./michael_run_bazel_build.sh

(15:30:04) ERROR: Skipping '//tflite/...': error loading package under directory 'tflite':
error loading package 'tflite/acceleration/configuration': Label '@local_xla//xla/tsl/platform/default:build_config.bzl' is invalid
because 'xla/tsl/platform/default' is not a package;
perhaps you meant to put the colon here: '@local_xla//xla/tsl:platform/default/build_config.bzl'?

(15:30:04) ERROR: error loading package under directory 'tflite':
error loading package 'tflite/acceleration/configuration': Label '@local_xla//xla/tsl/platform/default:build_config.bzl' is invalid
because 'xla/tsl/platform/default' is not a package;
perhaps you meant to put the colon here: '@local_xla//xla/tsl:platform/default/build_config.bzl'?

I tried:
cd tflite

rg 'local_xla//xla/tsl/platform/default:build_config.bzl'

experimental/acceleration/configuration/BUILD
22:load("@local_xla//xla/tsl/platform/default:build_config.bzl", "tf_proto_library_py")

acceleration/configuration/BUILD
23:load("@local_xla//xla/tsl/platform/default:build_config.bzl", "tf_proto_library_py")
```


### ChatGPT 
```
@local_xla: This refers to an external workspace defined in the WORKSPACE or MODULE.bazel file.
Bazel uses this to reference an external repository or local directory.
The name local_xla is an alias for this external repository.

//xla/tsl: This specifies the path within the local_xla workspace to the directory xla/tsl.

platform/default/build_config.bzl:
This is the relative path to the build_config.bzl file from the xla/tsl directory.

To find the fully qualified file path, do the following:

Locate the @local_xla Repository:

Check the WORKSPACE or MODULE.bazel file for the definition of local_xla. For example:
 
local_repository(
    name = "local_xla",
    path = "third_party/local_xla",
)
This indicates that @local_xla corresponds to the directory third_party/local_xla in your project.
Combine the Paths:

Append xla/tsl/platform/default/build_config.bzl to the path of local_xla.
Using the example above, the full-qualified file path would be:
 
third_party/local_xla/xla/tsl/platform/default/build_config.bzl
Verify the File Exists: Navigate to the directory and check if the file exists:
 
cd third_party/local_xla/xla/tsl/platform/default
ls build_config.bzl

pwd
/Users/mlubinsky/CODE/LiteRT_2/LiteRT

find . -name WORKSPACE
./WORKSPACE
./third_party/tensorflow/ci/official/wheel_test/WORKSPACE
./third_party/tensorflow/WORKSPACE
./third_party/tensorflow/third_party/xla/xla/mlir_hlo/WORKSPACE
./third_party/tensorflow/third_party/xla/WORKSPACE
./third_party/tensorflow/third_party/xla/third_party/tsl/WORKSPACE

find . -name MODULE.bazel
./MODULE.bazel
```

git submodule update --init --recursive  

bazel sync

```
This repository includes the core runtime and tools for deploying machine learning models on various devices.
For comprehensive documentation and additional resources, visit the official LiteRT page:

https://ai.google.dev/edge/litert

Please note that, as of now, the LiteRT repository is not intended for open-source development because it pulls in existing TensorFlow code via a git submodule.
The development team plans to evolve the repository to a point where developers can directly build and contribute.
Until then, contributions should be directed to the existing TensorFlow Lite repository. 
GITHUB

For installation, LiteRT supports Python versions 3.9, 3.10, and 3.11 on Linux and macOS.
Ensure you have the appropriate environment set up before integrating LiteRT into your projects. 
GITHUB
```
For building LiteRT with CMake, detailed instructions are available here:

https://ai.google.dev/edge/litert/build/cmake
```
This guide provides step-by-step instructions for building the LiteRT library using the CMake tool on various operating systems. 

```

For building LiteRT for ARM-based computers, refer to:

https://ai.google.dev/edge/litert/build/arm

```
This page describes how to build the LiteRT libraries for ARM-based computers,
supporting two build systems and their respective features. 
For understanding the C++ library for microcontrollers, visit:
```
https://ai.google.dev/edge/litert/microcontrollers/library
```
This document outlines the basic structure of the C++ library and provides information about creating your own project. 

For an overview of LiteRT for Microcontrollers, see:
```
https://ai.google.dev/edge/litert/microcontrollers/overview
```
This page provides an overview of LiteRT for Microcontrollers, designed to run machine learning models on devices with limited memory. 


For information on TensorFlow Lite Model Maker, refer to:
```

https://ai.google.dev/edge/litert/libraries/modify

```
Model Maker allows you to train a TensorFlow Lite model using custom datasets in just a few lines of code. 

For Maven Central repository information, see:
```
https://central.sonatype.com/artifact/io.github.google-ai-edge/litert
```
This page provides information about the LiteRT library artifact available in the Maven Central repository. 


To use LiteRT on your MacBook or Windows machine with the goal of deploying it to embedded firmware, you’ll need to follow these steps to set up, configure, and adapt LiteRT for your target environment.

1. Understand LiteRT and Its Purpose
-----------------------------------
LiteRT (Lightweight Runtime) is designed to execute neural network models efficiently in resource-constrained environments.
It can be used for deploying AI models to embedded firmware running on MCUs, DSPs, or other low-power hardware.

2. Set Up the Development Environment
On MacBook
-----------
Install Homebrew (if not already installed):
 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install required tools:
 
brew install bazel cmake ninja gcc
Install Python (for model conversion and utilities, if needed):
 
brew install python
pip install numpy tensorflow

On Windows
----------
Install Bazel:
Download and install from Bazel's website. https://bazel.build/
Add Bazel to your system PATH during installation.
Install CMake and Ninja:
Install from CMake and Ninja.
Ensure they’re accessible from the command line by adding them to the PATH.
Install Python and TensorFlow:
Install Python from python.org.
Install TensorFlow tools:
 
pip install numpy tensorflow

3. Download LiteRT Source Code
---------------------------------
Clone the LiteRT repository:
git clone  https://github.com/google-ai-edge/LiteRT
 
cd litert

4. Build LiteRT for Testing
-----------------------------
Build on MacBook or Windows:
Use Bazel to build the runtime:

bazel build //path/to/litert:litert
Replace //path/to/litert with the target specified in the LiteRT repository documentation.
This command compiles LiteRT for your development machine.
Test that the runtime builds correctly by running a test binary:

bazel test //path/to/litert:test_litert
Use Alternative Build Systems (if available):
Check for CMakeLists.txt in the repository to see if LiteRT supports CMake or Make builds.
If supported, follow the repository-specific instructions for these tools.

5. Prepare LiteRT for Embedded Firmware
----------------------------------------
Cross-Compiling for Your Target Platform
Identify the target embedded platform (e.g., ARM Cortex-M, RISC-V).
Install the appropriate cross-compilation toolchain:
For ARM: Install the GNU Arm Embedded Toolchain (link).
For RISC-V: Install the RISC-V GCC toolchain (link).
Build for the Target Architecture
Modify the build command to use the cross-compilation toolchain:

bazel build --config=<target_architecture> //path/to/litert:litert
Replace <target_architecture> with your platform-specific configuration (e.g., arm, riscv).

6. Convert AI Models for LiteRT
------------------------------   
If deploying neural network models, convert them into a format suitable for LiteRT:
Use TensorFlow Lite Converter:

import tensorflow as tf

model = tf.keras.models.load_model("model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)
Use the model.tflite file as input for LiteRT.

7. Deploy LiteRT to Firmware
---------------------------
Link LiteRT with Your Firmware:

Add the LiteRT library to your firmware project (e.g., .a or .lib file from Bazel build).
Initialize LiteRT in your firmware application.
Flash to the Device:

Use a suitable tool (e.g., OpenOCD, ST-Link, J-Link) to flash the firmware to your embedded device.

8. Test and Debug
------------------
Run tests on your embedded device to verify that LiteRT and the AI models function as expected.
Debug issues using a hardware debugger or by logging output to a serial console.
Optional: Optimize for Embedded Systems
Use LiteRT's configuration options to minimize runtime memory usage and execution time.
Quantize the AI model (e.g., convert to INT8) for better performance on embedded systems.

Let me know your specific target hardware, and I can provide tailored instructions for cross-compilation and deployment!



How to compile and run Google's LiteRT on firmware?
--------------------------------------------------
ChatGPT said:
 
To compile and run Google's LiteRT (a lightweight runtime often used for neural networks or embedded systems) on firmware,
follow these general steps.
The exact process may vary based on the specific hardware platform, toolchain, and firmware environment you are using.

1. Understand LiteRT and Your Target Hardware
-----------------------------------------------
LiteRT is typically designed for deployment on embedded systems with constrained resources.
Confirm your target hardware supports the requirements for LiteRT:
Processor architecture (e.g., ARM Cortex-M, RISC-V, etc.).
Memory and storage constraints.
Peripheral or OS capabilities (if any).

2. Set Up the Development Environment
-------------------------------
Install Required Tools
Install a suitable cross-compilation toolchain for your hardware:
For ARM: Use the GNU Arm Embedded Toolchain (download).
For RISC-V: Use the RISC-V GCC Toolchain.
Install CMake and Ninja (if required for LiteRT's build system).
Install any SDK or board support package (BSP) provided by your hardware vendor.
Download LiteRT
Clone or download the LiteRT source code:
 
git clone https://github.com/google/litert.git
cd litert

3. Configure LiteRT for Firmware
---------------------
Check the README.md or documentation provided with LiteRT to identify any specific build options for embedded platforms.
Modify LiteRT's configuration files as necessary:
Specify the target platform, architecture, and toolchain.
Configure memory allocation and optimization settings.
Example (if LiteRT uses CMake):

mkdir build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=path_to_toolchain.cmake -DLITERT_TARGET=embedded
Replace path_to_toolchain.cmake with the path to your toolchain file (specific to your hardware architecture).

4. Build LiteRT
-------------
Run the build command:

make
Or, if using Ninja:

ninja

The output will include a compiled LiteRT binary or library (e.g., .a or .elf file).

5. Integrate LiteRT with Firmware
-----------------------
Standalone LiteRT: If LiteRT runs directly on bare metal, link the LiteRT binary with your firmware application.
RTOS or OS Integration:
If your firmware uses an RTOS (e.g., FreeRTOS or Zephyr), integrate LiteRT into the RTOS project by adding it as a module or task.
Ensure LiteRT initialization code is called during the firmware startup.

6. Flash LiteRT Firmware to the Device
--------------------------------------
Connect your target hardware to your development machine.
Use the appropriate flashing tool:
For ARM Cortex-M devices: Use OpenOCD, ST-Link, or the vendor-provided flashing tool.
For RISC-V: Use J-Link or a similar debugger.
Example:

openocd -f interface/stlink.cfg -f target/stm32f4x.cfg -c "program build/output.elf verify reset exit"

7. Run and Test LiteRT
---------------------
Power on the hardware and monitor the output using a serial terminal (e.g., PuTTY, Tera Term) connected to the device's UART port.
Test LiteRT functionality by running example models or workloads provided in the LiteRT repository.

9. Debugging and Optimization
If the firmware does not work as expected, use debugging tools like GDB to identify issues.
Optimize LiteRT's performance and memory usage to suit your hardware's constraints.

```

<https://github.com/margaretmz/awesome-tflite>

https://blog.tensorflow.org/2023/03/tensorflow-with-matlab.html

https://ai.google.dev/edge/litert/microcontrollers/overview

http://rnd-jira.ssi.samsung.com:8080/browse/LOCSW-23824

## Sound

https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech/train 

https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/train/train_micro_speech_model.ipynb

https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/train/README.md

## TF Micro Build Op Registration
```
static tflite::MicroOpResolver<5> micro_op_resolver;
  micro_op_resolver.AddBuiltin(
      tflite::BuiltinOperator_DEPTHWISE_CONV_2D,
      tflite::ops::micro::Register_DEPTHWISE_CONV_2D(), 3);
  micro_op_resolver.AddBuiltin(tflite::BuiltinOperator_CONV_2D,
                               tflite::ops::micro::Register_CONV_2D(), 3);
  micro_op_resolver.AddBuiltin(tflite::BuiltinOperator_AVERAGE_POOL_2D,
                               tflite::ops::micro::Register_AVERAGE_POOL_2D(),2);
  micro_op_resolver.AddBuiltin(tflite::BuiltinOperator_RESHAPE,
                               tflite::ops::micro::Register_RESHAPE(),1);
  micro_op_resolver.AddBuiltin(tflite::BuiltinOperator_SOFTMAX,
                               tflite::ops::micro::Register_SOFTMAX(), 2);
			       
```

(mbed) (tf) [mbed]$ find . -name "*.cc" | xargs grep micro_op_resolver.Add

```
./tensorflow/lite/micro/examples/micro_speech/main_functions.cc:  if (micro_op_resolver.AddDepthwiseConv2D() != kTfLiteOk) {
./tensorflow/lite/micro/examples/micro_speech/main_functions.cc:  if (micro_op_resolver.AddFullyConnected() != kTfLiteOk) {
./tensorflow/lite/micro/examples/micro_speech/main_functions.cc:  if (micro_op_resolver.AddSoftmax() != kTfLiteOk) {
./tensorflow/lite/micro/examples/micro_speech/main_functions.cc:  if (micro_op_resolver.AddReshape() != kTfLiteOk) {
```

(mbed) (tf) [mbed]$ find . -name "*.cc" | xargs grep -i Logisti
```
./tensorflow/lite/micro/kernels/logistic.cc:#include "tensorflow/lite/kernels/internal/reference/integer_ops/logistic.h"
./tensorflow/lite/micro/kernels/logistic.cc:#include "tensorflow/lite/kernels/internal/reference/logistic.h"
./tensorflow/lite/micro/kernels/logistic.cc:TfLiteStatus LogisticEval(TfLiteContext* context, TfLiteNode* node) {
./tensorflow/lite/micro/kernels/logistic.cc:        reference_ops::Logistic(
./tensorflow/lite/micro/kernels/logistic.cc:        reference_integer_ops::Logistic(
./tensorflow/lite/micro/kernels/logistic.cc:TfLiteRegistration* Register_LOGISTIC() {
./tensorflow/lite/micro/kernels/logistic.cc:                                 /*invoke=*/activations::LogisticEval,
./tensorflow/lite/micro/all_ops_resolver.cc:  AddLogistic();
./tensorflow/lite/core/api/flatbuffer_conversions.cc:    case BuiltinOperator_LOGISTIC:			       
			       
```

### model.cc
 find . -type f | xargs grep g_model
``` 
./tensorflow/lite/micro/examples/micro_speech/micro_features/model.cc:const unsigned char g_model[] DATA_ALIGN_ATTRIBUTE = {
./tensorflow/lite/micro/examples/micro_speech/micro_features/model.cc:const int g_model_len = 18288;
./tensorflow/lite/micro/examples/micro_speech/micro_features/model.h:extern const unsigned char g_model[];
./tensorflow/lite/micro/examples/micro_speech/micro_features/model.h:extern const int g_model_len;
./tensorflow/lite/micro/examples/micro_speech/main_functions.cc:  model = tflite::GetModel(g_model);
```

<https://blog.tensorflow.org/search?label=TensorFlow+Lite&max-results=100>

<https://medium.com/yonohub/deep-learning-for-embedded-linux-series-part-1-model-optimization-daa553a5979>

To make predictions with our Keras model, we could just call the predict() method, passing an array of inputs. 

With TensorFlow Lite, we need to do the following: 
```
 - Instantiate an Interpreter object.
 - Call some methods that allocate memory for the model.
 - Write the input to the input tensor.
 - Invoke the model.
 - Read the output from the output tensor.
```


### Testing

 Macros are defined in the file micro_test.h . 
 TF_LITE_MICRO_TESTS_BEGIN 
 TF_LITE_MICRO_TEST  


  
### main_functions.cc 

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/main_functions.cc>

```
kXrange -  specifies the maximum possible x value as 2π, 
kInferencesPerCycle  - defines the number of inferences that we want to perform as we step from 0 to 2π. 
```

The next few lines of code calculate the x value: // Calculate an x value to feed into the model. We compare the current // inference_count to the number of inferences per cycle to determine // our position within the range of possible x values the model was // trained on, and use this to calculate a value. 

```
float position = static_cast < float > ( inference_count ) / static_cast < float > ( kInferencesPerCycle ); 
float x_val = position * kXrange ; 
```
The first two lines of code just divide inference_count (which is the number of inferences we’ve done so far) by kInferencesPerCycle to obtain our current “position” within the range. The next line multiplies that value by kXrange , which represents the maximum value in the range (2π). 
 . 
  last thing we do in our loop() function is increment our inference_count counter. If it has reached the maximum number of inferences per cycle defined in kInferencesPerCycle , we reset it to 0: 
  ```
  // Increment the inference_counter, and reset it if we have reached 
  // the total number per cycle 
  inference_count += 1 ; if ( inference_count >= kInferencesPerCycle ) inference_count = 0 ; 
  ```

The following cell runs xxd on our quantized model, writes the output to a file called sine_model_quantized.cc , and prints it to the screen 
Install xxd if it is not available ```apt-get qq install xxd```

  Save the file as a C source file
 ```
  xxd -i sine_model_quantized.tflite > sine_model_quantized.cc
 ``` 
  cat sine_model_quantized.cc 
  
  The output is very long, so we won’t reproduce it all here, but here’s a snippet that includes just the beginning and end: 
  
 ``` 
  unsigned char sine_model_quantized_tflite [] = {
  0x1c , 0x00 , 0x00 , 0x00 , 0x54 , 0x46 , 0x4c , 0x33 , 0x00 , 0x00 , 0x12 , 0x00 , 0x1c , 0x00 , 0x04 , 0x00 
  ...
  0x00 , 0x09 , 0x04 , 0x00 , 0x00 , 0x00 }; 
  unsigned int sine_model_quantized_tflite_len = 2512 ; 

```

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/sine_model_data.h>

// Create an area of memory to use for input, output, and intermediate arrays. 
// Finding the minimum value for your model may require some trial and error. 
```
const int tensor_arena_size = 2 × 1024 ; uint8_t tensor_arena [ tensor_arena_size ]; 


write our input data to the model’s input tensor: 
// Obtain a pointer to the model's input tensor 

TfLiteTensor * input = interpreter . input ( 0 ); 

```

```
In the example we’re walking through, our model accepts a scalar input, so we have to assign only one value
( input->data.f[0] = 0. ). 
If our model’s input was a vector consisting of several values, we would add them to subsequent memory locations. 
Here’s an example of a vector containing the numbers 1, 2, and 3: [1 2 3] 
And here’s how we might set these values in a TfLiteTensor : 

// Vector with 6 elements 
input > data . f [ 0 ] = 1. ; 
input > data . f [ 1 ] = 2. ; 
input > data . f [ 2 ] = 3. ;  


After we’ve set up the input tensor, it’s time to run inference. 
This is a one-liner: TfLiteStatus invoke_status = interpreter . Invoke (); 
 
 Reading the Output Like the input, our model’s output is accessed through a TfLiteTensor , and getting a pointer to it is just as simple: 
 
 TfLiteTensor * output = interpreter . output ( 0 ); 
 
 The output is, like the input, a floating-point scalar value nestled inside a 2D tensor. 
 
 we grab the output value and inspect it to make sure that it meets our high standards. First we assign it to a float variable: // Obtain the output value from the tensor float 
 
 value = output > data . f [ 0 ]; 
 
 Each time inference is run, the output tensor will be overwritten with new values. This means that if you want to keep an output value around in your program while continuing to run inference, you’ll need to copy it from the output tensor, 


main_functions.h, main_functions.cc 
A pair of files that define a setup() function, which performs all the initialization required by our program, and a loop() function, which contains the program’s core logic and is designed to be called repeatedly in a loop. These functions are called by main.cc when the program starts. 

output_handler.h, output_handler.cc 
A pair of files that define a function we can use to display an output each time inference is run. The default implementation, in output_handler.cc , prints the result to the screen. We can override this implementation so that it does different things on different devices. 

sine_model_data.h, sine_model_data.cc 
A pair of files that define an array of data representing our model, as exported using xxd in the first part of this chapter. 

The file output_handler.cc defines our HandleOutput() function. Its implementation is very simple:

void HandleOutput ( tflite :: ErrorReporter * error_reporter , float x_value , float y_value ) { 
// Log the current X and Y values 
error_reporter > Report ( "x_value: %f, y_value: %f \n " , x_value , y_value ); 
} 

 
```



### Udacity free TF 2 course

<https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187>

<https://habr.com/ru/post/453482/>

### Book
<https://github.com/ageron> 

<https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646/> BOOK

<http://www.aicheatsheets.com/>

<http://aicheatsheets.com/tensorflow1.html>

<https://www.reddit.com/r/Python/comments/cyslju/ai_cheatsheets_now_learn_tensorflow_keras_pytorch/>

<https://www.reddit.com/r/learnmachinelearning/comments/daw0vn/handson_machine_learning_with_scikitlearn_and/>

<https://icenamor.github.io/files/books/Hands-on-Machine-Learning-with-Scikit-2E.pdf> BOOK

<https://github.com/ageron/handson-ml2>

 

## Keras

<https://habr.com/ru/post/482126/>

<https://www.reddit.com/r/learnmachinelearning/comments/czkf78/learn_keras_in_one_video/>

<https://habr.com/ru/company/ods/blog/325432/>

<https://habr.com/ru/post/453558/>

<https://habr.com/ru/company/ruvds/blog/486686/>

<https://kite.com/blog/python/python-machine-learning-keras>

<https://towardsdatascience.com/boost-your-cnn-image-classifier-performance-with-progressive-resizing-in-keras-a7d96da06e20>

<https://autokeras.com/>

<https://www.youtube.com/playlist?list=PLJ1jRXwHYGNpSKcSVm117e5hy_xTwsNrS>

<https://www.youtube.com/playlist?list=PLlb7e2G7aSpT1ntsozWmWJ4kGUsUs141Y>

<https://www.youtube.com/watch?v=RKKhzFBmEBg>  Лекция 2. Нейронные сети. Теория и первый пример (Анализ данных на Python в примерах и задачах. Ч2)

<https://www.youtube.com/watch?v=F0tlV4W62AU>  Лекция 4. Обучение нейронных сетей в Keras, ч. 2 (Анализ данных на Python в примерах и задачах. Ч2)

<https://medium.com/intuitive-deep-learning/build-your-first-convolutional-neural-network-to-recognize-images-84b9c78fe0ce>

<https://github.com/keras-team/keras/tree/master/examples>

<https://habr.com/ru/post/331382/> Auto-encoders

```
cat ~/.keras/keras.json
{
    "epsilon": 1e-07,
    "floatx": "float32",
    "image_data_format": "channels_last",
    "backend": "tensorflow"
}
```

переведем номер класса в так называемый one-hot вектор, т.е. вектор, состоящий из нулей и одной единицы:
```
y_train = keras.utils.to_categorical(newsgroups_train["target"], num_classes)

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
	      
```

## Tensorflow

<https://www.youtube.com/watch?v=JdXxaZcQer8&list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf&index=9>

<https://habr.com/ru/post/465745/> 

<https://habr.com/ru/post/453482/> Введение в глубокое обучение с использованием TensorFlow

<https://habr.com/ru/post/453558/>

<https://www.techrepublic.com/article/beginners-guide-for-tensorflow-the-basics-of-googles-machine-learning-library/?ftag=TREe09998f&bhid=35141061>

<https://www.edyoda.com/course/1429> Step by step guide to Tensorflow

<https://habr.com/ru/company/ods/blog/324898/>

<https://towardsdatascience.com/guide-to-coding-a-custom-convolutional-neural-network-in-tensorflow-bec694e36ad3>

<https://blog.exxactcorp.com/deep-learning-with-tensorflow-training-resnet-50-from-scratch-using-the-imagenet-dataset/>

<https://medium.com/tensorflow/structural-time-series-modeling-in-tensorflow-probability-344edac24083>

<https://hackernoon.com/tensorflow-is-dead-long-live-tensorflow-49d3e975cf04?sk=37e6842c552284444f12c71b871d3640>  TF 2.0 alpha

## Classes
<https://www.coursera.org/learn/introduction-tensorflow/home/welcome>

<https://classroom.udacity.com/courses/ud187>


<https://github.com/taki0112/Tensorflow-Cookbook>

<https://learningtensorflow.com/index.html>

<https://medium.com/tensorflow>

<https://arxiv.org/pdf/1610.01178.pdf>

<https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/>

<https://medium.com/devseed/technical-walkthrough-packaging-ml-models-for-inference-with-tf-serving-2a50f73ce6f8>

<https://youtu.be/LSb8iaNAfdw> .  Russian

<https://github.com/astorfi/TensorFlow-World>

<https://github.com/TensorImage/TensorImage>

<https://habr.com/post/428183/>

Linear regression:
<https://medium.com/@derekchia/a-line-by-line-laymans-guide-to-linear-regression-using-tensorflow-3c0392aa9e1f>
```
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def generate_dataset():
	x_batch = np.linspace(0, 2, 100)
	y_batch = 1.5 * x_batch + np.random.randn(*x_batch.shape) * 0.2 + 0.5
	return x_batch, y_batch

def linear_regression():
	x = tf.placeholder(tf.float32, shape=(None, ), name='x')
	y = tf.placeholder(tf.float32, shape=(None, ), name='y')

	with tf.variable_scope('lreg') as scope:
		w = tf.Variable(np.random.normal(), name='W')
		b = tf.Variable(np.random.normal(), name='b')
		
		y_pred = tf.add(tf.multiply(w, x), b)

		loss = tf.reduce_mean(tf.square(y_pred - y))

	return x, y, y_pred, loss

def run():
	x_batch, y_batch = generate_dataset()

	x, y, y_pred, loss = linear_regression()

	optimizer = tf.train.GradientDescentOptimizer(0.1)
	train_op = optimizer.minimize(loss)

	with tf.Session() as session:
		session.run(tf.global_variables_initializer())

		feed_dict = {x: x_batch, y: y_batch}
		
		for i in range(30):
			_ = session.run(train_op, feed_dict)
			print(i, "loss:", loss.eval(feed_dict))

		print('Predicting')
		y_pred_batch = session.run(y_pred, {x : x_batch})

	plt.scatter(x_batch, y_batch)
	plt.plot(x_batch, y_pred_batch, color='red')
	plt.xlim(0, 2)
	plt.ylim(0, 2)
	plt.savefig('plot.png')

if __name__ == "__main__":
	run()
``` 

<https://github.com/open-source-for-science/TensorFlow-Course>

<https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md>

<https://twitter.com/hashtag/tensorflowjs>

<https://tf.wiki/en/preface.html> . 
 
<https://colab.research.google.com/> 

<https://www.tensorflow.org/lite/>

<https://medium.com/tensorflow/training-and-serving-ml-models-with-tf-keras-fd975cc0fa27>
 
<https://www.youtube.com/watch?v=tYYVSEHq-io&t=3664s>

<https://www.youtube.com/watch?v=tjsHSIG8I08>

<https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ> 

<https://becominghuman.ai/an-introduction-to-tensorflow-f4f31e3ea1c0>
 
<https://medium.com/@tensorflow>

<https://habrahabr.ru/search/?q=tensorflow>

<https://github.com/tensorflow/workshops>

<https://medium.com/tensorflow/introducing-tensorflow-probability-dca4c304e245>

<https://colab.research.google.com/>

<https://www.youtube.com/watch?v=tYYVSEHq-io>

<http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.66230&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false>
 
