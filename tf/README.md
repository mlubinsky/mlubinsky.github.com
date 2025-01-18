<https://builtin.com/machine-learning/introduction-deep-learning-tensorflow-20>

<https://habr.com/ru/post/500788/>


## TFLite   LiteRT

https://ai.google.dev/edge/litert

https://github.com/google-ai-edge/LiteRT

```
LiteRT, formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.
The project's source code is available on GitHub:

https://github.com/google-ai-edge/LiteRT

c:\GIT\LiteRT>C:\Users\m.lubinsky\Downloads\bazel-8.0.0-windows-x86_64.exe build LiteRT:litert
INFO: Reading 'startup' options from c:\git\litert\.bazelrc: --windows_enable_symlinks
INFO: Options provided by the client:
  Inherited 'common' options: --isatty=1 --terminal_columns=142
INFO: Reading rc options for 'build' from c:\git\litert\.bazelrc:
  Inherited 'common' options: --experimental_repo_remote_exec --experimental_repo_remote_exec
INFO: Options provided by the client:
  'build' options: --python_path=C:/Users/m.lubinsky/AppData/Local/Programs/Python/Python38/python.exe
INFO: Reading rc options for 'build' from c:\git\litert\.bazelrc:
  'build' options: --define framework_shared_object=true --define tsl_protobuf_header_only=true --define=use_fast_cpp_protos=true --define=allow_oversize_protos=true --spawn_strategy=standalone -c opt --announce_rc --define=grpc_no_ares=true --noincompatible_remove_legacy_whole_archive --features=-force_no_whole_archive --enable_platform_specific_config --define=with_xla_support=true --config=short_logs --experimental_cc_shared_library --experimental_link_static_libraries_once=false --incompatible_enforce_config_setting_visibility --config=v2 --config=litert_prefixes
INFO: Found applicable config definition build:short_logs in file c:\git\litert\.bazelrc: --output_filter=DONT_MATCH_ANYTHING
INFO: Found applicable config definition build:v2 in file c:\git\litert\.bazelrc: --define=tf_api_version=2 --action_env=TF2_BEHAVIOR=1
INFO: Found applicable config definition build:litert_prefixes in file c:\git\litert\.bazelrc: --define=litert_prefixes=external/org_tensorflow/
INFO: Found applicable config definition build:windows in file c:\git\litert\.bazelrc: --copt=/W0 --host_copt=/W0 --copt=/Zc:__cplusplus --host_copt=/Zc:__cplusplus --copt=/D_USE_MATH_DEFINES --host_copt=/D_USE_MATH_DEFINES --features=compiler_param_file --features=archive_param_file --copt=/d2ReducedOptimizeHugeFunctions --host_copt=/d2ReducedOptimizeHugeFunctions --copt=-D_ENABLE_EXTENDED_ALIGNED_STORAGE --host_copt=-D_ENABLE_EXTENDED_ALIGNED_STORAGE --enable_runfiles --cxxopt=/std:c++17 --host_cxxopt=/std:c++17 --config=monolithic --copt=-DWIN32_LEAN_AND_MEAN --host_copt=-DWIN32_LEAN_AND_MEAN --copt=-DNOGDI --host_copt=-DNOGDI --copt=/Zc:preprocessor --host_copt=/Zc:preprocessor --linkopt=/DEBUG --host_linkopt=/DEBUG --linkopt=/OPT:REF --host_linkopt=/OPT:REF --linkopt=/OPT:ICF --host_linkopt=/OPT:ICF --verbose_failures --features=compiler_param_file
INFO: Found applicable config definition build:monolithic in file c:\git\litert\.bazelrc: --define framework_shared_object=false --define tsl_protobuf_header_only=false --experimental_link_static_libraries_once=false
WARNING: --enable_bzlmod is set, but no MODULE.bazel file was found at the workspace root. Bazel will create an empty MODULE.bazel file. Please consider migrating your external dependencies from WORKSPACE to MODULE.bazel. For more details, please refer to https://github.com/bazelbuild/bazel/issues/18958.
ERROR: Error computing the main repository mapping: Error accessing registry https://bcr.bazel.build/: Failed to fetch registry file https://bcr.bazel.build/modules/rules_shell/0.2.0/MODULE.bazel: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
ERROR: Error while writing profile file: Cannot create symlink (name=C:\users\m.lubinsky\_bazel_m.lubinsky\7ry3bayt\command.profile.gz, target=C:\users\m.lubinsky\_bazel_m.lubinsky\7ry3bayt\command-c77bf3a2-5af7-4775-8433-4014f9c5cf00.profile.gz): ERROR: src/main/native/windows/file-jni.cc(140): nativeCreateSymlink(\\?\C:\users\m.lubinsky\_bazel_m.lubinsky\7ry3bayt\command.profile.gz, \\?\C:\users\m.lubinsky\_bazel_m.lubinsky\7ry3bayt\command-c77bf3a2-5af7-4775-8433-4014f9c5cf00.profile.gz): ERROR: src/main/native/windows/file.cc(524): CreateSymlink(\\?\C:\users\m.lubinsky\_bazel_m.lubinsky\7ry3bayt\command-c77bf3a2-5af7-4775-8433-4014f9c5cf00.profile.gz): createSymbolicLinkW failed (permission denied). Either Windows developer mode or admin privileges are required.
Computing main repo mapping:

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
 
