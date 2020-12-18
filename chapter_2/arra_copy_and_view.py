import numpy as np

x2 = np.random.randint(10, size=(3, 4))

print(x2)

x2_sub = x2[:2, :2]
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub)

x2_sub[0, 0] = 99
x2[1, 1] = 100
print(x2)

print(x2_sub)
print(x2_sub_copy)
