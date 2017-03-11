#  python-course.eu/numpy.php
#  python-course.eu/matrix_ariphmetics.php
#  http://www.bogotobogo.com/python/python_numpy_matrix_tutorial.php
#  http://www.bogotobogo.com/python/python_numpy_array_tutorial_basic_B.php
# https://blog.drskippy.com/2012/05/14/dimension-reduction-for-machine-learning-simple-example-of-svd-pca-pathology://blog.drskippy.com/2012/05/14/dimension-reduction-for-machine-learning-simple-example-of-svd-pca-pathology/
import time
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

one_int= np.ones((4,2), dtype=int)
print one
print one_int

print "transpose"
print one.transpose()

print "----- IDENTITY -----"
i=np.eye(3)
j=np.identity(3)
print i
print j
print i.shape
print "Identity transpose"
print i.transpose()

print "------  RAND in (0-1) interval -------"
rand= np.random.random((20)) #in range 0-1
print rand

print "-- Matrix "
A = np.array([[1,2],[3,4]])
print A
print "sum=", A.sum(), A.sum(axis=0), A.sum(axis=1)
print "mean=", A.mean(), A.mean(axis=0),  A.mean(axis=1)
print "min=", A.min()
print "max=", A.max()
print "std=", A.std()


print " ----eigenvector -------"

eig_val, eig_vec= eig(A)
print eig_val
print eig_vec

print "--DOT PRODUCT--"

print "------  COL -------"
col= np.array([1,2,3])
print col
print "shape=", col.shape, " size=",  col.size
print "inneri with himself =", col.dot(col)
print "outer with himself=", np.outer(col,col)
print "cross with himself=", np.cross(col,col)

print "------  ROW -------"
row= np.array([[1,2,3]])
print row
print "shape=", row.shape, " size=",  row.size
print "transpose row ", row.T
print "x*x.T ", row*row.T
print "x.T * x ", row.T * row
print "cross with himself=", np.cross(row,row)


print "--INNER PRODUCT  for 1d vectors  is just a number (scalar product) "
print np.inner(col,row)
print np.inner(row,col)
print np.inner(row,row)

print "-- Cross product of vectors is a vector which is ortogonal to both vectors and length=|a| |b| sin(a,b)"
print np.cross(col,row)
print np.cross(row,col)

print "----linspace-----"
print np.linspace(0,10,5, endpoint=True)
print np.linspace(0,10,5, endpoint=False)

time.sleep(20)
