import numpy as np

# fmt: off
Z2Y = np.array([
    [1, 0,  0, 0],
    [0, 0,  1, 0],
    [0, -1, 0, 0],
    [0, 0,  0, 1]
])

Y2Z = np.array([
    [1, 0, 0, 0],
    [0, 0, -1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])

X2Y = np.array([
    [0, 0, -1, 0],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, 0, 1]
])

Y2X = np.array([
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

X2Z = np.array([
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
])

Z2X = np.array([
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])