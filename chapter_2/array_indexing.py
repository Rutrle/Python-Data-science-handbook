import numpy as np

x1 = np.random.randint(10, size=6)  # one dimensional array
x2 = np.random.randint(10, size=(3, 4))  # one dimensional array


print(x1)

print(x1[0])
print(x1[4])
print(x1[-1], '\n')


print(x2)
print(x2[0, 0], '\n')

x2[0, 0] = 12
print(x2)
