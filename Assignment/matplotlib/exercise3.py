import matplotlib.pyplot as plt
import numpy as np

# 이거 좀 수정

data = np.random.randn(200, 5)
plt.boxplot(data)
plt.title("box plot")
plt.show()
