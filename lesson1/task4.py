import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = np.cos(x)
y2 = np.cos(1.1 * x)

plt.plot(x, y1, marker='o')
plt.plot(x, y2, marker='o')
plt.show()