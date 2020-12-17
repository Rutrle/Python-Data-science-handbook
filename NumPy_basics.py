import numpy as np
import array

print(np.__version__)

# python buil-in array

L = list(range(10))
A = array.array('i', L)
print(A)


# Numpy arrays

# integer array
B = np.array([1, 4, 2, 5, 3])
print(B)

# upcast from integer to float
C = np.array([3.14, 5, 6, 4])
print(C)

# set type of numpy array:
D = np.array([1, 2, 3, 4], dtype='float32')
print(D)

# multiple dimensions
E = np.array([range(i, i+3) for i in [2, 4, 6]])
print(E)
