# Dealing with Rows and Columns in Pandas DataFrame....
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.

import pandas as pd

df = pd.read_csv('nba.csv')
print(df)
# ======================================================================================================================
# Dealing with Columns:----
# Column Selection

cols = df.columns
print(cols)

# Access a single column with thier column name...
print(df['Name'])

# Access multiple columns with their column name..
print(df[['Name', 'Age', 'Weight']])

# ======================================================================================================================
# # Declare a list that is to be converted into a column
address = 'Delhi'

# # Using 'Address' as the column name, it will be add new column in df. If you pass the list of address name then
# lenght will be same as index has it is.
df['Address'] = address
print(df)

# ======================================================================================================================
# Column Deletion: ------
# In Order to delete a column in Pandas DataFrame, we can use the drop() method..

# drop the column by their column name......
df.drop(['Address', 'Weight'], axis= 1, inplace= True)
print(df)

# ======================================================================================================================

# Dealing with Rows:---------
# In order to deal with rows, we can perform basic operations on rows like selecting, deleting, adding and renaming.

# Row Selection,,,
# Pandas provide a unique method to retrieve rows from a Data frame.
# DataFrame.loc[]
# method is used to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to an
# iloc[] function.

print(df.iloc[0])

