import numpy as np

import numpy as np
np.random.seed(0)

# computing reciprocals one by one


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


values = np.random.randint(1, 10, size=5)
big_array = np.random.randint(1, 10, size=10000000)

print(1/values)
'''
# slow way
compute_reciprocals(big_array)

# numpy quick way
result = 1/big_array
'''
# multiple arrays
print(np.arange(5) / np.arange(1, 6))
# more dimensions
x = np.arange(9).reshape((3, 3))
print(2 ** x)
