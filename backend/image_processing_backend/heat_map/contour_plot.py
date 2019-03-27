# library & dataset
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

print(df)

# Basic 2D density plot
sns.set_style("white")
sns.kdeplot(df.sepal_width, df.sepal_length)
plt.show()

# # Custom it with the same argument as 1D density plot
sns.kdeplot(df.sepal_width, df.sepal_length, cmap="Reds", shade=True, bw=.15)

# Some features are characteristic of 2D: color palette and wether or not color the lowest range
# sns.kdeplot(df.sepal_width, df.sepal_length, cmap="Blues", shade=True, shade_lowest=True, )
plt.show()
