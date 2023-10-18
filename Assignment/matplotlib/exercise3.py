import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(200, 5)
plt.boxplot(data, notch=True)
plt.title("box plot")
plt.show()
