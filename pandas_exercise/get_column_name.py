# Syntax to Get Column Names in Pandas
# # Get column names as an Index object
# column_names = df.columns


import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head())

cols = df.columns
print(cols)
for col in cols:
    print(col)

# Get Column Names in Pandas column.values
# The column.values method returns an array of index.
print(df.columns.values)


# Pandas List Column Names using tolist() Method
# Using tolist() method with values with given the list of columns.

print(df.columns.tolist())

print(df.columns.values.tolist())

sorted(df)
print(df.columns.values.tolist())

# =====================================================================================================================
# How to rename columns in Pandas DataFrame
# Pandas Rename Column
#
# df.rename(columns={'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}, inplace=True)
# Rename Column Pandas using rename()
df.rename(columns={'Name': 'NAME'}, inplace=True)
print(df.head())

# Pandas Rename Column by Assigning a List of new Column Names
# The columns can also be renamed by directly assigning a list containing the new names to the columns attribute
#   of the Dataframe object for which we want to rename the columns.
# The disadvantage of this method is that we need to provide new names for all the columns even
#   if want to rename only some of the columns.


# rename multiple columns.....
# We can rename multiple columns in a Pandas DataFrame
# using a dictionary with old column names as keys and new column names as values passed to the rename() method.
df.rename(columns={'NAME':'Name', 'Age':'AGE', 'Salary':'SALARY'}, inplace=True)
print(df.head())


# Pandas Rename Column by Assigning a List of new Column Names....but their has a one disadvantage.......
# The disadvantage of this method is that we need to provide new names for all the columns.
#   even if want to rename only some of the columns.

# -----------------------------------------------------------------------------------------------------------------

# Add Prefix Sufix to Rename Column Name in Pandas DataFrame.....

df.rename(columns={'Name':'N_Name'}, inplace=True)
print(df.head())
df = df.add_prefix('X_')
df = df.add_suffix('_1')
print(df.head())

# ----------------------------------------------------------------------------------------------------------------------

# Pandas Replace a character in Column Name...
#  we will rename the column name using the replace function, we will pass the old name with the new name as a parameter for the column.

df.columns = df.columns.str.replace('X_N_Name_1', 'Name')
print(df.columns)

# ==============================================================================================================
# How do I get a specific column name in Pandas?
# Get all column name
cols = df.columns
print(cols)

# Get a specific column name using index in columns.
col = df.columns[1]
print(col)

# Get all columns name as a list
all_col = df.columns.tolist()
print(all_col)


