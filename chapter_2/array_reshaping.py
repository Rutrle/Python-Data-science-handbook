import numpy as np

# changing shape with reshape
grid = np.arange(1, 10).reshape(3, 3)

print(grid)


x = np.array([1, 2, 3])
# row vector via reshape
print(x.reshape((1, 3)))
# row vector via newaxis
print(x[np.newaxis, :])

# to columne via reshape and newaxis:
print(x.reshape((3, 1)))
# row vector via newaxis
print(x[:, np.newaxis])
