import numpy as np
# general pattern is x[start:stop:step]

x = np.arange(10)
print(x)

# first 5 elements
print(x[:5])

# elements after index 5
print(x[5:])

# elements in the middle
print(x[4:7])

# every other element
print(x[::2])

# every other element, starting from 1
print(x[1::2])


# reversing array
print(x[::-1])

# reversing part of array
print(x[5:2:-1])
