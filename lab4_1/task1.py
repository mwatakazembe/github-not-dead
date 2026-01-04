import matplotlib.pyplot as plt
import numpy as np
import math

x_degrees = np.linspace(-360, 360, 1000)
x_radians = np.radians(x_degrees)

f_x = []
for i in range(len(x_degrees)):
    x_rad = x_radians[i]
    term1 = math.exp(math.cos(x_rad))
    term2 = math.log((math.cos(0.6 * x_rad))**2 + 1) * math.sin(x_rad)
    f_x.append(term1 + term2)

h_x = []
for i in range(len(x_degrees)):
    x_rad = x_radians[i]
    term = (math.cos(x_rad) + math.sin(x_rad))**2 + 2.5
    h_x.append(-math.log(term) + 10)

plt.figure(figsize=(12, 8))
plt.plot(x_degrees, f_x, 'b-', linewidth=2, label='f(x) = e^(cos(x)) + ln(cos²(0.6x) + 1) · sin(x)')
plt.plot(x_degrees, h_x, 'r-', linewidth=2, label='h(x) = -ln((cos(x) + sin(x))² + 2.5) + 10')

plt.xlabel('degrees', fontsize=12)
plt.ylabel('function value', fontsize=12)
plt.title('function graphs from -360° to 360°', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

plt.xlim(-360, 360)
plt.xticks(np.arange(-360, 361, 90))

plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()