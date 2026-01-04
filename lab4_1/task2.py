import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-10, -3.1, 1000)
x2 = np.linspace(-2.9, 2.9, 1000)
x3 = np.linspace(3.1, 10, 1000)
y1 = 5 / (x1**2 - 9)
y2 = 5 / (x2**2 - 9)
y3 = 5 / (x3**2 - 9)


plt.plot(x1, y1, 'b', x2, y2, 'b', x3, y3, 'b')
plt.ylim(-10, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 5 / (x^2 - 9)')
plt.grid(True)
plt.show()