import numpy as np

# basic operations
x = np.arange(4)
print("x = ", x)
print("x + 5 = ", x+5)
print("x - 5 = ", x-5)
print("x * 2 = ", x*2)
print("x / 2 = ", x/2)
print("x // 2 = ", x//2)

print('-x =', -x)
print("x ** 2 = ", x**2)
print("x % 2 = ", x % 2)

# standard order of operations works
print(-(0.5*x + 1) ** 2)

print(np.add(x, 2))
