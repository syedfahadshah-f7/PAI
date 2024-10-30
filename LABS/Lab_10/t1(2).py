import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("heart.csv")
# plt.figure(figsize=(15,15))
# sns.heatmap(data=df.corr(), annot = True)
# plt.show()


# sns.displot(data=df, x="age",kde=True,edgecolor=None)
# plt.show()

# x = df["sex"].value_counts()
# plt.pie(x, labels=["Male", "Female"], autopct='%1.1f%%')
# plt.show()

sns.scatterplot(data=df, x="age", y="thalach", hue="target")
plt.show()