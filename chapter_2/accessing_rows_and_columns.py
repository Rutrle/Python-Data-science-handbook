import numpy as np

x2 = np.random.randint(10, size=(3, 4))
print(x2)

# whole first column
print(x2[:, 0])

# whole first row
print(x2[0, :])

# alternative
print(x2[0])
