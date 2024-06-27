# Pandas
# Pandas is a powerful and widely-used open-source data manipulation and analysis library for Python.
# It provides data structures and functions needed to work with structured data seamlessly and efficiently.

# Importing Pandas
import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:\n", s)

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Arun', 'Bhavna', 'Chirag'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Reading data from a CSV file (assuming 'data.csv' exists in the working directory)
# df = pd.read_csv('data.csv')

# Writing data to a CSV file
# df.to_csv('output.csv', index=False)

# DATA MANIPULATION 
# Selecting a column
ages = df['Age']
print("\nAges:\n", ages)

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)

# Grouping and aggregating data
grouped = df.groupby('City').mean()
print("\nGrouped by City:\n", grouped)

# Handling missing data
df = df.dropna()  # Drop rows with any missing values
print("\nDataFrame after dropping NaNs:\n", df)
df = df.fillna(0)  # Fill missing values with 0
print("\nDataFrame after filling NaNs with 0:\n", df)

# WORKING WITH PANDAS IN A TIME SERIES
# Creating a date range
rng = pd.date_range('2024-01-01', periods=10, freq='D')
print("\nDate Range:\n", rng)

# Creating a DataFrame with a time index
ts = pd.Series(np.random.randn(10), index=rng)
print("\nTime Series:\n", ts)

# Basic Operations:
# Indexing and Selecting Data
# Selecting a column: You can select a column from a DataFrame using the column label.
ages = df['Age']
print("\nAges Column:\n", ages)

# Selecting rows by label: Use the loc attribute for label-based indexing.
row = df.loc[0]  # First row
print("\nFirst Row:\n", row)

rows = df.loc[0:1]  # First two rows
print("\nFirst Two Rows:\n", rows)

# Filtering Data
# Filtering allows you to select rows that meet certain conditions.
# Selecting rows where Age > 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)

# Visualization
# Pandas integrates with Matplotlib for data visualization:

# Plotting a DataFrame
df.plot(kind='bar')
plt.show()
