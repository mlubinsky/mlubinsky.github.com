#  http://www.bogotobogo.com/python/python_numpy_matrix_tutorial.php
#  http://www.bogotobogo.com/python/python_numpy_array_tutorial_basic_B.php
# https://blog.drskippy.com/2012/05/14/dimension-reduction-for-machine-learning-simple-example-of-svd-pca-pathology://blog.drskippy.com/2012/05/14/dimension-reduction-for-machine-learning-simple-example-of-svd-pca-pathology/

import numpy as np
from numpy.linalg import eig
np.show_config()
print np.version.version

print "----- ZERO -----"
zero=np.zeros((2,4))
print zero
print zero.shape


print "----- ONE -----"
one= np.ones((4,2))
print one
print "transpose"
print one.transpose()

print "----- DENTITY -----"
i=np.eye(3)
print i
print i.shape
print "transpose"
print i.transpose()

print "------  RAND -------"
rand= np.random.random((2,2)) #in range 0-1

print "------  COL -------"
col= np.array([1,2,3])
print col
print col.shape
print col.size

print "------  ROW -------"
row= np.array([[1,2,3]])
print row
print row.shape
print row.size

print " ----eigenvector -------"
A = np.array([[1,2],[3,4]])
eig_val, eig_vec= eig(A)
print eig_val
print eig_vec

