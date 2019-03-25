## Keras
<https://habr.com/ru/company/ods/blog/325432/>

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

<https://www.edyoda.com/course/1429> Step by step guide to Tensorflow

<https://habr.com/ru/company/ods/blog/324898/>

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
 
