#https://medium.com/@mjfstanford/simple-linear-regression-in-python-905b759ef0e6
import numpy as np
import matplotlib.pyplot as plt

noise=np.random.uniform(-20,20,100)
X = np.linspace(0, 100,100)+noise
y = np.linspace(0,50,100)+noise


denominator=X.dot(X) -X.mean() *X.sum()
m = ( X.dot(y) - y.mean() *X.sum()) / denominator
b = ( y.mean() * X.dot(X) - X.mean()*X.dot(y)) /denominator
y_pred = m*X + b

# Plot the points using matplotlib
plt.plot(X, y_pred,'r')
plt.scatter(X,y)
plt.show()  # You must call plt.show() to make graphics appear


