import numpy as np

x1 = np.random.randint(10, size=6)  # one dimensional array
x2 = np.random.randint(10, size=(3, 4))  # one dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # one dimensional array

print(x1)
print(x2)
print(x3)

print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("x3 dtype: ", x3.dtype)

print("x3 itemsize: ", x3.itemsize, "bytes")
print("x3 nbytes: ", x3.nbytes, "bytes")
