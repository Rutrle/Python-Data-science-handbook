import numpy as np
# general pattern is x[start:stop:step]

x2 = np.random.randint(10, size=(3, 4))

print(x2)


# first two rows, first three columns
print(x2[:2, :3])

# all rows, every other column
print(x2[:3, ::2])

# reverse all
print(x2[::-1, ::-1])
