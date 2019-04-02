# https://towardsdatascience.com/guide-to-coding-a-custom-convolutional-neural-network-in-tensorflow-bec694e36ad3

import os

import tensorflow as tf
import numpy as np
from tqdm import tqdm
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# MNIST Dataset
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()
train_images  = np.expand_dims(train_images.astype(np.float32) / 255.0, axis=3)
test_images = np.expand_dims(test_images.astype(np.float32) / 255.0, axis=3)
train_labels = to_categorical(train_labels)

# Training parameters
batch_size = 128
n_epochs = 5
n_classes = 10
learning_rate = 1e-4

# 2D Convolutional Function
def conv2d(x, W, b, strides=1):
    x = tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)

# Define Weights and Biases
weights = {
    # Convolution Layers
    'c1': tf.get_variable('W1', shape=(3,3,1,16), \
            initializer=tf.contrib.layers.xavier_initializer()),
    'c2': tf.get_variable('W2', shape=(3,3,16,16), \
            initializer=tf.contrib.layers.xavier_initializer()),
    'c3': tf.get_variable('W3', shape=(3,3,16,32), \
            initializer=tf.contrib.layers.xavier_initializer()),
    'c4': tf.get_variable('W4', shape=(3,3,32,32), \
            initializer=tf.contrib.layers.xavier_initializer()),

    # Dense Layers
    'd1': tf.get_variable('W5', shape=(7*7*32,128),
            initializer=tf.contrib.layers.xavier_initializer()),
    'out': tf.get_variable('W6', shape=(128,n_classes),
            initializer=tf.contrib.layers.xavier_initializer()),
}
biases = {
    # Convolution Layers
    'c1': tf.get_variable('B1', shape=(16), initializer=tf.zeros_initializer()),
    'c2': tf.get_variable('B2', shape=(16), initializer=tf.zeros_initializer()),
    'c3': tf.get_variable('B3', shape=(32), initializer=tf.zeros_initializer()),
    'c4': tf.get_variable('B4', shape=(32), initializer=tf.zeros_initializer()),

    # Dense Layers
    'd1': tf.get_variable('B5', shape=(128), initializer=tf.zeros_initializer()),
    'out': tf.get_variable('B6', shape=(n_classes), initializer=tf.zeros_initializer()),
}

# Model Function
def conv_net(data, weights, biases, training=False):
    # Convolution layers
    conv1 = conv2d(data, weights['c1'], biases['c1']) # [28,28,16]
    conv2 = conv2d(conv1, weights['c2'], biases['c2']) # [28,28,16]
    pool1 = tf.nn.max_pool(conv2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
    # [14,14,16]

    conv3 = conv2d(pool1, weights['c3'], biases['c3']) # [14,14,32]
    conv4 = conv2d(conv3, weights['c4'], biases['c4']) # [14,14,32]
    pool2 = tf.nn.max_pool(conv4, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')
    # [7,7,32]

    # Flatten
    flat = tf.reshape(pool2, [-1, weights['d1'].get_shape().as_list()[0]])
    # [7*7*32] = [1568]

    # Fully connected layer
    fc1 = tf.add(tf.matmul(flat, weights['d1']), biases['d1']) # [128]
    fc1 = tf.nn.relu(fc1) # [128]

    # Dropout
    if training:
        #fc1 = tf.nn.dropout(fc1, rate=0.2)
        fc1 = tf.nn.dropout(fc1, keep_prob=0.8)

    # Output
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out']) # [10]
    return out

# Dataflow Graph
dataset = tf.data.Dataset.from_tensor_slices((train_images,train_labels)).repeat().batch(batch_size)
iterator = dataset.make_initializable_iterator()
batch_images, batch_labels = iterator.get_next()
logits = conv_net(batch_images, weights, biases, training=True)
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=batch_labels))
optimizer = tf.train.AdamOptimizer(learning_rate)
train_op = optimizer.minimize(loss)
test_predictions = tf.nn.softmax(conv_net(test_images, weights, biases))
acc,acc_op = tf.metrics.accuracy(predictions=tf.argmax(test_predictions,1), labels=test_labels)

# Run Session
with tf.Session() as sess:
    # Initialize Variables
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    sess.run(iterator.initializer)

    # Train the Model
    for epoch in range(n_epochs):
        prog_bar = tqdm(range(int(len(train_images)/batch_size)))
        for step in prog_bar:
            _,cost = sess.run([train_op,loss])
            prog_bar.set_description("cost: {:.3f}".format(cost))
        accuracy = sess.run(acc_op)

        print('\nEpoch {} Accuracy: {:.3f}'.format(epoch+1, accuracy))

    # Show Sample Predictions
    predictions = sess.run(tf.argmax(conv_net(test_images[:25], weights, biases), axis=1))
    f, axarr = plt.subplots(5, 5, figsize=(25,25))
    for idx in range(25):
        axarr[int(idx/5), idx%5].imshow(np.squeeze(test_images[idx]), cmap='gray')
        axarr[int(idx/5), idx%5].set_title(str(predictions[idx]),fontsize=50)

    # Save Model
    saver = tf.train.Saver()
    saver.save(sess, './model.ckpt')

