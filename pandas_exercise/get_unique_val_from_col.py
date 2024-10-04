# Get unique values from a column in Pandas DataFrame...
# The unique() function removes all duplicate values on a column and returns a single value for multiple same values.

#
# # Get the unique values of any column
# df.ColumnName.unique()

# Creating a Pandas Dataframe with Duplicate Elements......

# Create a sample Pandas dataframe with a dictionary list ....

# Import pandas module...
import pandas as pd

data = {'A':['A1', 'A2', 'A3', 'A4', 'A5','NaN', 'NaN'],
'B':['B1', 'B2', 'B3', 'B4', 'B4','NaN', 'NaN'],
'C':['C1', 'C2', 'C3', 'C3', 'C3','NaN', 'NaN'],
'D':['D1', 'D2', 'D2', 'D2', 'D2','NaN', 'NaN'],
'E':['E1', 'E1', 'E1', 'E1', 'E1','NaN', 'NaN']}

# Covert dictionary list into pandas Dataframe.. with set index name.

df = pd.DataFrame(data).set_index('A').rename_axis('Col Name', axis=1)
print(df)

print(df.index.name)

print(df.columns.name)

df = df.rename_axis('foo')
print(df)

df = df.rename_axis(index=None, columns=None)
print(df)


# ----------------------------------------------------------------------------------------------------------------------
# Get unique valune any of the column here column'B'.
unique_B_val = df['B'].unique() # df.B.unique()
print(unique_B_val)

# Eliminate Duplicate Values from a Column using set()

# # Use set() to eliminate duplicate values in column 'C'

unique_val = set(df['C'])
print(unique_val)

# Remove duplicate with NaN values........and return duplicate with single value
df['B'] = df['B'].drop_duplicates()
df['C'] = df['C'].drop_duplicates()
print(df)


# Count unique value.... also count NaN


# How to handle NaN values when getting unique data in Pandas?......



# # Remove NaN values and get unique values....  None and NaN in dataframe are same
unique_B_val_only = df['D'].dropna().unique()
print(unique_B_val_only)

unique_count = df['D'].dropna().nunique()
print(unique_count)

df_with_nan = pd.DataFrame({'A': [1, 2, 2, None, 4, None]})
# Remove NaN values and get unique values
unique_values = df_with_nan['A'].dropna().unique()

print(unique_values)




