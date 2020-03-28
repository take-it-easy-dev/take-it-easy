import numpy as np
import math

OFFSET = np.array([160., 0.])

DELTA = 100

BASIS_1 = DELTA/math.sqrt(2) * np.array([-1., -0.7])
BASIS_2 = DELTA/math.sqrt(2) * np.array([1., -0.7])

BASE_COORDS = {
    1:  [0, 0],
    2:  [1, 0],
    3:  [0, 1],
    4:  [2, 0],
    5:  [1, 1],
    6:  [0, 2],
    7:  [2, 1],
    8:  [1, 2],
    9:  [3, 1],
    10: [2, 2],
    11: [1, 3],
    12: [3, 2],
    13: [2, 3],
    14: [4, 2],
    15: [3, 3],
    16: [2, 4],
    17: [4, 3],
    18: [3, 4],
    19: [4, 4],
}

COORDINATES = {
    i: OFFSET + arr[0] * BASIS_1 + arr[1] * BASIS_2 for i, arr in BASE_COORDS.items()
}

with open('dot_positions.css', 'w') as f:
    for i, coord in COORDINATES.items():
        x, y = int(coord[0]), int(coord[1])
        f.write(f".dot{i}" + "{\n")
        f.write(f"  left: {x}px;\n")
        f.write(f"  top: {-y}px;\n")
        f.write("}\n\n")

