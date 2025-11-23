import pandas as pd
import matplotlib.pyplot as plt

# Load UCI Iris Dataset
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
df.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']

# Line Plot
df.plot()
plt.show()

# Histogram
df.hist()
plt.show()

# Scatter Plot
df.plot.scatter(x='SepalLength', y='PetalWidth')
plt.show()

# Box Plot
df.plot.box()
plt.show()
