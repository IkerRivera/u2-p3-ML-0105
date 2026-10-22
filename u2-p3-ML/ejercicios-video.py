# Array indexing in NumPy
import numpy as np

n0105 = np.array([10, 20, 30, 40, 50])
print(n0105)
print(n0105[0])
print(n0105[3])
print(n0105[-1])
print(n0105[-2])
print("----------------------------------------")

n0105 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n0105)
print(n0105[0, 0])
print(n0105[1, 2])
print(n0105[-1, -1])
print(n0105[-2, -2])
print("----------------------------------------")

# 3D array 2x(2x3)
n0105 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0105)
print(n0105[0, 0, 0])
print("Iker Montoya 0105")