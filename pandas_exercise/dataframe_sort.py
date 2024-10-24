# Python | Pandas Dataframe.sort_values()
# Pandas sort_values() function sorts a data frame in Ascending or Descending order of passed Column


# Syntax: DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
#
#
# Note: Every parameter has some default values except the ‘by’ parameter.

# Return Type:
#
#
# Returns a sorted Data Frame with Same dimensions as of the function caller DataFrame.

import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())

df = df.sort_values('Name', axis=0)
print(df.head())
