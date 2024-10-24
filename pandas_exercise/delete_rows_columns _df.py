# Python | Delete rows/columns from DataFrame using Pandas.drop()

# Pandas DataFrame drop() Method Syntax
#
# Syntax: DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors=’raise’)

# Parameters:
#
#
# labels: String or list of strings referring row or column name.
# axis: int or string value, 0 ‘index’ for Rows and 1 ‘columns’ for Columns.
# index or columns: Single label or list. index or columns are an alternative to axis and cannot be used together. level: Used to specify level in case data frame is having multiple level index.
# inplace: Makes changes in original Data Frame if True.
# errors: Ignores error if any value from the list doesn’t exists and drops rest of the values when errors = ‘ignore’
#
# Return type: Dataframe with dropped values



# # dropping passed values
# data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace = True)
#


# # dropping passed columns
# data.drop(["Team", "Weight"], axis = 1, inplace = True)
#
# # display
# print(data.head())


