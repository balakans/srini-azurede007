import pandas as pd

df = pd.read_csv('D:\Training\pycharmworkouts\Data\TopRichestInWorld.csv')

#Get structure & quick summary: df.info()
print(df.info())

print("===Get data types: df.dtypes===")
print(df.dtypes)

print("===Get shape (rows, columns): df.shape===")
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

print("===Get number of rows: len(df) or df.shape[0]===")
print(len(df))         # OR
print(df.shape[0])

print("===Get number of columns: df.shape[1]===")
print(df.shape[1])

print("=== Get column names: df.columns===")
print(df.columns)

print("===Get index (row labels): df.index===")
print(df.index)

print("===Get summary statistics: df.describe()===")
print(df.describe())
print(df.describe(include="all"))

print("===Check for nulls: df.isnull().sum()===")
print(df.isnull().sum())

print("===Get first or last few rows: df.head() / df.tail()===")
print(df.head(1))   # First row
print(df.tail(1))   # Last row

print("===Check memory usage: df.memory_usage()===")
print(df.memory_usage())

print("===Check unique values in a column===")
print(df['Age'].unique())
