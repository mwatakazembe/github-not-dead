import numpy as np

A = np.array([
    [-2, -8.5, -3.4, 3.5],
    [0, 2.4, 0, 8.2],
    [2.5, 1.6, 2.1, 3],
    [0.3, -0.4, -4.8, 4.6]
])

B = np.array([-1.88, -3.28, -0.5, -2.83])

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
X_rounded = np.round(X, 1)

print("solution vector x:")
print(X_rounded)