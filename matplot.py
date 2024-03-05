import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# * Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 5))
# ! Every plt.show creates a window and show all the plots that werent shown before
# ! data.head() shows the dataframe to see its content

# * Line chart
points = np.array([4, 7, 2, 10, 13])
axes[0, 0].plot(points, linestyle="dotted")
axes[0, 0].set_title("Example line dotted")

# * Bar chart
x = np.array(["X", "Y", "Z", "W"])
y = np.array([25, 30, 27, 22])
axes[0, 1].bar(x, y)
axes[0, 1].set_title("Example bar plot")

# * Scatter plot
x1 = np.array([20, 15, 11, 7, 8, 10])
y1 = np.array([2, 7, 15, 8, 10, 12])
axes[1, 0].scatter(x1, y1)
axes[1, 0].set_title("Example scatter plot")

# * Pie chart
p = np.array([35, 20, 25, 20])
axes[1, 1].pie(p)
axes[1, 1].set_title("Example pie plot")

# * Histogram
h1 = np.random.normal(170, 10, 250)
axes[2, 0].hist(h1)
axes[2, 0].set_title("Example hist plot")

# * Remove the empty subplot in the second column of the third row to show only the other plot in the full row
fig.delaxes(axes[2, 1])

# * Adjust layout to prevent overlapping and show it
plt.tight_layout()
plt.show()

# * Seaborn box plot (shows statiscal values in the plot)
df = sns.load_dataset("tips")
df.boxplot(by="day", column=["total_bill"], grid=False)
plt.show()

# * Seaborn dist plot (histogram)
titanic = sns.load_dataset("titanic")
age1 = titanic["age"].dropna()  # * Remove nan or other wrong values
sns.displot(age1, bins=30, kde=False)
plt.show()

# * Seaborn reg plot (Linear regression and scatter)
data = sns.load_dataset("mpg")
sns.regplot(x="mpg", y="acceleration", data=data)
plt.show()
