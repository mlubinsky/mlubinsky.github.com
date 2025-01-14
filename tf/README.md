<https://builtin.com/machine-learning/introduction-deep-learning-tensorflow-20>

<https://habr.com/ru/post/500788/>


## TFLite

https://ai.google.dev/edge/litert

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
 
