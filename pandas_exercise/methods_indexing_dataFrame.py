# Methods for indexing in DataFrame............
import  pandas as pd
df = pd.read_csv('nba.csv', index_col='Name')
print(df)
# Python | Pandas Dataframe/Series.head() method.....

# Pandas head() method is used to return top n (5 by default) rows of a data frame or series.
# Syntax: Dataframe.head(n=5)
# Parameters:
#
# n: integer value, number of rows to be returned

# Return type: Dataframe with top n rows

top_data = df.head()
print(top_data)

series_data = df['College']
print(series_data)

# Pandas tail() method is used to return bottom n (5 by default) rows of a data frame or series.
last_data = df.tail()
print(last_data)


# Python | Pandas Dataframe.at[ ]....
# Pandas at[] is used to return data in a dataframe at the passed location.
# The passed location is in the format [position, Column Name]. This method works in a similar way
# to Pandas loc[ ] but at[ ] is used to return an only single value and hence works faster than it.


position = 'Shelvin Mack'
label = 'College'

# calling .at[] method
output = df.at[position, label]

# display
print(output)


# Python | Pandas Dataframe.iat[ ]
# Pandas iat[] method is used to return data in a dataframe at the passed location.
# The passed location is in the format [position in the row, position in the column].
# This method works similarly to Pandas iloc[] but iat[] is used to return only a single value and hence works faster than it.




#--------------------------------------------
# Python | Pandas Dataframe.pop()
# the pandas pop method can take input of a column from a data frame and pop that directly.
# Syntax: DataFrame.pop(item)
# Parameters:
# item: Column name to be popped in string
# Return type: Popped column in form of Pandas Series

new_df = df.copy()

# Example #2: Popping and pushing in other data frame
pop_col = df.pop('College')

#create new dataframe with column pop_column
new_df['pop_column'] = pop_col
print(new_df.head())

# Python | Pandas dataframe.insert()........
# Pandas insert method allows the user to insert a column in a data frame or series(1-D Data frame).
# Syntax:
#
# DataFrameName.insert(loc, column, value, allow_duplicates = False)
#
# Parameters:
# loc: loc is an integer which is the location of column where we want to insert new column.
# This will shift the existing column at that position to the right.
# column: column is a string which is name of column to be inserted.
# value: value is simply the value to be inserted. It can be int, string,
# float or anything or even series / List of values.
# Providing only one value will set the same value for all rows.
# allow_duplicates : allow_duplicates is a boolean value which checks if column with same name already exists or not.

# Add Column with Static Value to Pandas Dataframe. All rows will be same value.

print(df.columns)

df['Gender'] = 'Male'
print(df)

# Pandas Add Multiple Columns to DataFrame.......
# Insert New Multiple Columns into the DataFrame
new_columns_data = {'New1': [160, 175, 168, 0],
                    'New2': [55, 70, 65, 0]}

new_columns_df = pd.DataFrame(new_columns_data)

# Combine the original df with new columns dataframe...

result_df = pd.concat([df, new_columns_df], axis=1)
print(result_df.head())

# Add column to Pandas using DataFrame.insert()
df.insert(1, 'New1', new_columns_df['New1'])
print(df)

# Insert Calculated Column in Pandas using dataframe.insert()

df.insert(1, 'New_Weight', df['Weight'] + 1)
print(df)
df.insert(1, 'Age_Status', ['Adult' if age >= 18 else 'Minor' for age in df['Age']])

print(df)


# Python | Pandas dataframe.get()
# Pandas dataframe.get() function is used to get item from object for given key.
# The key could be one or more than one dataframe column. It returns default value if not found.
print(df.get('Age_Status'))

# Example #2: Use get() function to extract multiple columns at a time in random order.
# The ordering of the columns is not according to the actual dataframe but it follows the ordering that
# we provided to it in the function input.
print(df.get(['Age_Status', 'Age', 'Team']))

# ----------------------------------------------------------------------------------------------------------------------
# Python | Pandas DataFrame.isin()
# Syntax: DataFrame.isin(values)
#
# Parameters: values: iterable, Series, List, Tuple,
#   DataFrame or dictionary to check in the caller Series/Data Frame.
#
# Return Type: DataFrame of Boolean of Dimension.

# Single Parameter filtering Using Pandas DataFrame.isin()
# The DataFrame.isin() method in Pandas is a powerful tool for filtering and selecting data within a DataFrame based on specified conditions.
#

# Rows are checked and a boolean series is returned which is True wherever Age_Status=”Adult”.
# Return boolean series
filter1_data = df['Age_Status'].isin(['Adult'])
print(filter1_data)

# Then the series is passed to the data frame to see new filtered data frame.
print(df[filter1_data])



# Multiple Parameter filtering.......
# # creating filters of bool series from isin()
filter2_data = df['Team'].isin(['Boston Celtics','Utah Jazz'])

# # displaying data with both filter applied and mandatory
print(df[filter1_data & filter2_data])


# Python | Pandas DataFrame.where()....
# Pandas where() method in Python is used to check a data frame for one or more conditions and return
# the result accordingly. By default, The rows not satisfying the condition are filled with NaN value.
# Syntax: DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors=’raise’, try_cast=False, raise_on_error=None)
# Parameters:
#
#
# cond: One or more condition to check data frame for.
# other: Replace rows which don’t satisfy the condition with user defined object, Default is NaN
# inplace: Boolean value, Makes changes in data frame itself if True
# axis: axis to check( row or columns)

# Pandas DataFrame.where() Single Condition Operation......

# # making boolean series for a team name
team_filter = df['Team'] == 'Boston Celtics'
print(team_filter)
age_filter = df['Age'] >= 27

# Every row which doesn’t have Team = Boston Celtics  is replaced with NaN.
df.where(team_filter & age_filter, inplace=True)
print(df)


# Pandas dataframe.mask() function
# The mask method is an application of the if-then idiom.
# Syntax: DataFrame.mask(cond, other=nan, inplace=False, axis=None, level=None, errors=’raise’, try_cast=False, raise_on_error=None)

df.mask(team_filter, 'My New Team', inplace=True)
print(df)

df.mask(df.isna(), 1000, inplace=True)
print(df)

# -------------------------------------------------------------------------------------------------------
# Pandas DataFrame query() Method
# Dataframe.query() method only works if the column name doesn’t have any empty spaces. So before applying the method,
# spaces in column names are replaced with ‘_’ .

df.columns = [column.replace(" ", "_") for column in df.columns]

print(df.columns)
df.query('Team == "My New Team"', inplace=True)
print(df)



