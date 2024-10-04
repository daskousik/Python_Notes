# Python | Delete rows/columns from DataFrame using Pandas.drop()
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages.
# Pandas is one of those packages which makes importing and analyzing data much easier.

# Pandas DataFrame drop() Method Syntax......
# Syntax: DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors=’raise’)

# Parameters:
#
#
# labels: String or list of strings referring row or column name.
# axis: int or string value, 0 ‘index’ for Rows and 1 ‘columns’ for Columns.
# index or columns: Single label or list. index or columns are an alternative to axis and cannot be used together.
# level: Used to specify level in case data frame is having multiple level index.
# inplace: Makes changes in original Data Frame if True.
# errors: Ignores error if any value from the list doesn’t exists and drops rest of the values when errors = ‘ignore’

# Return type: Dataframe with dropped values.....

# # importing pandas module
import pandas as pd

# load csv file into dataframe using pandas
df = pd.read_csv('nba.csv', index_col='Name')

print(df.head())
print(df['Age']) # Column name has case-sensitive

# Selecting rows using loc method for string , We have also iloc method for integer index.
print(df.loc[['Avery Bradley', 'Jae Crowder']])

# # dropping passed values with row name
print(df.drop(['Avery Bradley', 'Jae Crowder'], inplace=True))

# Dropping column name with axis 1

print(df.drop(['Height', 'Age'], axis= 1, inplace=True))
print(df)



# Extract rows between two index labels

rows = df.loc["John Holland":"Kelly Olynyk"]
print(rows)


