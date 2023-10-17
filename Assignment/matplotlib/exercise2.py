import matplotlib.pyplot as plt
import numpy as np


N = 60
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)
area = np.pi * (
    15 * np.random.rand(N))**2.4
plt.scatter(x, y,
            s=area, c=colors,
            alpha=0.7)

plt.show()
