# Iterating over rows and columns in Pandas DataFrame

#  Pandas DataFrame consists of rows and columns
#  so, to iterate over dataframe, we have to iterate a dataframe like a dictionary.

# In Pandas Dataframe we can iterate an element in two ways:
#
# Iterating over Rows
# Iterating over Columns


# In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples()
# Iteration Over Rows in Pandas using iterrows()
# Example 1: Row Iteration Using iterrows()

# Example 1: Row Iteration Using iterrows()
#
# In order to iterate over rows,
# we apply a iterrows() function this function returns each index value along with a series containing the data in each row.

import pandas as pd

df = pd.read_csv('nba.csv')

print(df.loc[:, ['Age']])
# iterating over rows using iterrows() function

# returns each index value along with a series containing the data in each row.
for i, j in df.head(2).iterrows():
    print(i)
    print(j)

# Example 1: Row Iteration Using iteritems()
#
# In order to iterate over rows, we use iteritems() function
# this function iterates over each column as key, value pair with the label as key, and column value as a Series object.

for i in df.head(2).itertuples():
    print(i)


# Pandas Iterate Over Columns of DataFrame
# Example 1: Pandas Column Iteration
#
# In order to iterate over columns, we need to create a list of dataframe columns and
# then iterating through that list to pull out the dataframe columns.

cols = list(df)
print(cols)

# iterate over column with rows...
for i in cols:
    print(df[i][2])

# ========================================================================================================================

# How to iterate over rows and columns in Pandas DataFrame?
# To iterate over rows, you can use the iterrows() method, which yields both the index and the row as a Series:

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6] })
#
for index, row in df.iterrows():
    print(f"Index: {index}, Row: {row['A'], row['B']}")


# To iterate over columns, you can simply loop through the DataFrame:

print(df)
for column in df:
    print(f"column {column} , Data {df[column]}")

# How to interchange rows and columns in Pandas DataFrame?
# To transpose rows and columns, effectively interchanging them, use the T attribute or transpose() method:

df_transpose = df.T
print(df_transpose)


# How to access row and column in Pandas DataFrame?
# To access rows and columns by label, use loc:
#
# # Access a specific row by index label
# row = df.loc[0]
#
# # Access a specific column
# column = df.loc[:, 'A']
# print(row, column)

# How to swap two rows in a DataFrame in Python?
# Swap rows 0 and 2
df.loc[[0, 2]] = df.loc[[2, 0]].values

print(df)


column = df.loc[:, ['A']]
print(column)
