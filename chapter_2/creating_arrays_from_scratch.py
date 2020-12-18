import numpy as np

A = np.zeros(10, dtype=int)

print(A)

B = np.ones((3, 5), dtype=float)

print(B)

C = np.full((4, 4), 3.14)

print(C)

# array filled with linear sequence
D = np.arange(0, 20, 2)
print(D)

# create array ov values between two given values:
E = np.linspace(0, 1, 5)
print(E)

# create random 3 * 3 array wih numbers distributed between 0 and 1
F = np.random.random((3, 3))
print(F)

# create random 3 x 3 array withmean 1 and standard debiation 1:

G = np.random.normal(0, 1, (3, 3))
print(G)

# creates a random array with numbers between 0 and 10

H = np.random.randint(0, 10, (3, 3))
print(H)

# creates a identity matrix 3 x 3
I = np.eye(3)
print(I)

# creates uninitialized array, values are whatever is currently at the memory location
J = np.empty(3)
print(J)
