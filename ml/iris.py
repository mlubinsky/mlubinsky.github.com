# http://krisbolton.com/a-practical-introduction-to-artificial-neural-networks-with-python/
# The Iris dataset consists of 150 samples of four features per sample, measuring the length and width of sepals and petals (in cm), with 50 samples
# for three species of Iris (Iris setosa, Iris virginica, and Iris versicolor).

# The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
# Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
# Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

# The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import numpy as np

iris = datasets.load_iris()
x = iris.data
y = iris.target

print x[:5]
print y[:5]

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot graph
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xticks(())
plt.yticks(())

plt.show()

# Set aside 30% of the data set for training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# The StandardScaler() function standardised all of the features in a dataset to have a mean and unit variance of zero, to ensure all of the features are distributed normally. Many predictive algorithms require the data set to be standardised otherwise their behavior will be unpredictable.

# Train the scaler, which standarises all the features to have mean and unit variance of zero
sc = StandardScaler()
sc.fit(x_train)

# Now we apply the scaler to each section of the split data set.

# Apply the scaler to the X training data
x_train_std = sc.transform(x_train)

# Apply the SAME scaler to the X test data
x_test_std = sc.transform(x_test)

# Create a perceptron object with 50 iterations over the data set, and a learning rate of 0.3
ppn = Perceptron(max_iter=50, eta0=1, verbose=0)

# Train the perceptron
ppn.fit(x_train_std, y_train)

Perceptron(alpha=0.0001, class_weight=None, eta0=1, fit_intercept=True,
      max_iter=50, n_iter=None, n_jobs=1, penalty=None, random_state=0,
      shuffle=True, tol=None, verbose=0, warm_start=False)

# Apply the trained perceptron on the X data to make predicts for the y test data
y_pred = ppn.predict(x_test_std)


# Print the accuracy of the implementation
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))


