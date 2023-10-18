import matplotlib.pyplot as plt
import seaborn as sns


titanic = sns.load_dataset("titanic")

sns.violinplot(x=titanic.pclass, y=titanic.fare, hue=titanic.survived)
plt.show()
