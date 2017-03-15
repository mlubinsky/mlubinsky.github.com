# https://www.datacamp.com/community/tutorials/machine-learning-python
import numpy as np
from sklearn import datasets
digits = datasets.load_digits()
#print(digits)
import matplotlib
print "config dir=", matplotlib.get_configdir()
matplotlib.use('TkAgg')
# the same dataset as above but from another location
#import pandas as pd
#digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)
print " ---- KEYS ------"
print digits.keys()

print " ----  DATA  ----"
print digits.data

print "  == DESCR ==="
#print digits.DESCR

# Isolate the `digits` data
digits_data = digits.data

print "there are 1797 samples and that there are 64 features "
# Inspect the shape
print(digits_data.shape)

# Isolate the target values with `target`
digits_target = digits.target

# Inspect the shape
print(digits_target.shape)

# Print the number of unique labels
number_digits = len(np.unique(digits.target))
print " # of unique labels=", number_digits

# Isolate the `images`
digits_images = digits.images

# Inspect the shape
print(digits_images.shape)

import matplotlib.pyplot as plt

# Figure size (width, height) in inches
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))


print "BEFORE SHOW"
# Show the plot
plt.show()
print "AFTERE SHOW"

