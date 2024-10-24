# Indexing in Pandas : Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.

# Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns,
# or some of each of the rows and columns. Indexing can also be known as Subset Selection.

# Pandas Indexing using [ ], .loc[], .iloc[ ], .ix[ ]

# Dataframe.[ ] ; This function also known as indexing operator
# Dataframe.loc[ ] : This function is used for labels...
# Dataframe.iloc[ ] : This function is used for positions or integer based.
# Dataframe.ix[] : This function is used for both label and integer based

# Collectively, they are called the indexers.
# These are four function which help in getting the elements, rows, and columns from a DataFrame.

import pandas as pd

df = pd.read_csv('nba.csv', index_col='Name')

print(df.head(10))

# Selecting a single columns Team
# In order to select a single column, we simply put the name of the column in-between the brackets
print(df['Team'])

# Selecting multiple columns..
# In order to select multiple columns, we have to pass a list of columns name in an indexing operator.
print(df[['Team', 'College', 'Salary']].head(5))

# In Order to select specific columns and rows ..
df = df[['Team', 'College', 'Salary']].loc[['Avery Bradley', 'Jeff Withey']]

print(df)

# Selecting a single row
# In order to select a single row using .loc[] , we put a single row label in a .loc function.
## retrieving row by loc method
print(df.loc['Avery Bradley'])

# Selecting multiple rows
# In order to select multiple rows, we put all the row labels in a list and pass that to .loc function.

#   print(df.loc[['R.J. Hunter', 'Amir Johnson']])

# Selecting two rows and three columns

# In order to select two rows and three columns, we select a two rows which we want to select and three columns and
# put it in a separate list like this:

# Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]
print(df.loc[['Avery Bradley', 'Jeff Withey'], ['Team', 'College', 'Salary']])


# Selecting all of the rows and some columns
# In order to select all of the rows and some columns, we use single colon [:] to select all of rows and list of
# some columns which we want to select like this:
# Dataframe.loc[:, ["column1", "column2", "column3"]]
print(df.loc[:, ['Team', 'College']])

# Indexing a DataFrame using .iloc[ ] :...
# This function allows us to retrieve rows and columns by position. In order to do that, we’ll need to
# specify the positions of the rows that we want, and the positions of the columns that we want as well.
# The df.iloc indexer is very similar to df.loc but only uses integer locations to make its selections.

# Retreving all rows and 1 position column name in the df.
print(df.iloc[:, [1]])

# ======================================================================================================================
# What is indexing and selecting data with Pandas in Python?.....
# Indexing and selecting data with pandas involve specifying which data points (rows and columns) in a
# DataFrame or Series you want to access or modify.
# Pandas provides powerful tools for selecting data based on label indexing, integer indexing, or condition-based filtering.


# How to select data based on index in Pandas?................
# We can select data based on the index using the loc and iloc attributes:
# loc: Used for label-based indexing.specify row labels and the names of columns you want to select.
#iloc: Used for integer position-based indexing. specify row and column numbers, which are zero-based integers.


# What is indexing method.................................?
# The indexing method refers to the technique used to organize and access data within a
# data structure (like a DataFrame or a Series in pandas).
# These methods are crucial for optimizing data retrieval, updates, and management.
# They define how data is internally stored and how efficiently you can retrieve or manipulate it.

# What are the methods of indexing in pandas....................?
# Label-based indexing (loc): Selects data based on data index value labels.
# Integer-based indexing (iloc): Selects data based on the integer position of rows and columns.
# Boolean indexing: Uses a boolean vector to filter data.
# Conditional indexing: Uses conditions to filter rows or columns.
# MultiIndex (hierarchical): Advanced indexing on multiple levels of index rows or columns.

#What are types of indexing?.......
# Single-level indexing: Regular index with a single label for each entry.
# Multi-level indexing (Hierarchical): Multiple index levels, allowing for more complex data arrangements.
# Datetime indexing: Specific to time series data, allowing date and time-based indexing.
# Interval indexing: For data indexed by ranges of values.
# Categorical indexing: For data categorized based on specific criteria.
