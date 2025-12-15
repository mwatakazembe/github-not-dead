import numpy as np
from scipy import integrate

def f_single(x):
    return np.exp(-x) * np.sin(x)

def f_double(x, y):
    return np.exp(-(x**2 + y**2))

result_single, error_single = integrate.quad(f_single, 0, np.pi)
result_double, error_double = integrate.dblquad(f_double, -1, 1, lambda x: -1, lambda x: 1)

print("definite integral result:")
print(round(result_single, 4))
print("double integral result:")
print(round(result_double, 4))