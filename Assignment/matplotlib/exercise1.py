import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

x = np.linspace(-1, 1, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)
y5 = x ** 2

ax1 = plt.subplot(311)
ax1.set_title("sin")
plt.plot(x, y1)
ax2 = plt.subplot(323)
ax2.set_title("cos")
plt.plot(x, y2)
ax3 = plt.subplot(324)
ax3.set_title("tan")
plt.plot(x, y3)
ax4 = plt.subplot(313)
ax4.set_title("x**2")
plt.plot(x, y5)

plt.show()
