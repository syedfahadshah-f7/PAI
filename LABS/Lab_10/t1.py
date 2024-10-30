import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("heart.csv")
plt.figure(figsize=(10,10))
plt.subplot(4,4,1)
sns.histplot(data= df,x="age")
plt.title("Age")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()

plt.subplot(4,4,2)
sns.histplot(data=df,x="cp")
plt.title("CPT")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()

plt.subplot(4,4,3)
sns.histplot(data=df,x="trestbps")
plt.title("EIA")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()

plt.subplot(4,4,4)
sns.histplot(data=df,x="fbs")
plt.title("FBS")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()

plt.show()