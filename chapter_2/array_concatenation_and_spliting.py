import numpy as np
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

print(np.concatenate([x, y]))

z = [99, 99, 99]
# also working with more arrays
print(np.concatenate([x, y, z]), '\n'*2)

# for multi-dimensional arrays
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid)
print(np.concatenate([grid, grid]))

# concatenate along the second axis (zero-indexed)
print(np.concatenate([grid, grid], axis=1))

# np.vstack for vertical stack, np.hstack for horizontal stack
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])

print(np.vstack([x, grid]))

y = np.array([[99], [99]])
print(np.hstack([grid, y]))


