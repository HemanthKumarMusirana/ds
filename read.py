import pandas as pd

# Read text file
df_txt = pd.read_table("data.txt")

# Read Excel file
df_excel = pd.read_excel("data.xlsx")

# Read data from web (Iris Dataset)
df_iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# Name columns manually for Iris
df_iris.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']

# Descriptive analytics
print(df_iris.head())
print(df_iris.info())
print(df_iris.describe())
