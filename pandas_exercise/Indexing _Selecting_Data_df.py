# Indexing in Pandas : Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.

# Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns,
# or some of each of the rows and columns. Indexing can also be known as Subset Selection.

# Pandas Indexing using [ ], .loc[], .iloc[ ], .ix[ ]

# Dataframe.[ ] ; This function also known as indexing operator
# Dataframe.loc[ ] : This function is used for labels...
# Dataframe.iloc[ ] : This function is used for positions or integer based.
# Dataframe.ix[] : This function is used for both label and integer based
import pandas as pd

df = pd.read_csv('nba.csv', index_col='Name')

print(df.head(10))

# Selecting a single columns Team
# In order to select a single column, we simply put the name of the column in-between the brackets
print(df['Team'])

# Selecting multiple columns..
# In order to select multiple columns, we have to pass a list of columns in an indexing operator.
print([['Team', 'College', 'Salary']])


df = df[['Team', 'College', 'Salary']].loc[['Avery Bradley', 'Jeff Withey']]

print(df)
#