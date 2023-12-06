import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 11, 1)
f_x = x ** 2

plt.plot(x, f_x)

x_new = 10
derivative = [x_new]
y = [x_new ** 2]
learning_rate = 0.9

for i in range(100):
    old_value = x_new
    x_new = old_value - learning_rate * 2 * old_value
    derivative.append(x_new)
    y.append(x_new ** 2)

plt.plot(x, f_x)
plt.plot(derivative, y, "bo-")
plt.show()
