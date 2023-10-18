import matplotlib.pyplot as plt
import seaborn as sns


titanic = sns.load_dataset("titanic")
# print(type(titanic))

sns.set_style("whitegrid")
sns.lineplot(x=titanic.age, y=titanic.fare, style=titanic.sex)

plt.show()
