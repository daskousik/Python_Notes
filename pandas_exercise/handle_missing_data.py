# Working with Missing Data in Pandas
# Missing Data can also refer to as NA(Not Available) values in pandas.


# In Pandas missing data is represented by two value:
#
# None: None is a Python singleton object that is often used for missing data in Python code.
# NaN : NaN (an acronym for Not a Number), is a special floating-point value recognized by all systems
# that use the standard IEEE floating-point representation.


# There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :
#
# isnull()
# notnull()
# dropna()
# fillna()
# replace()
# interpolate()

import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head())

# Checking for missing values using isnull() and notnull()
# In order to check missing values in Pandas DataFrame, we use a function isnull() and notnull().
# Both function help in checking whether a value is NaN or not.

# Checking for missing values using isnull()
# we use isnull() function this function return dataframe of Boolean values which are True for NaN values.

# return Boolean for all columns and rows. True for NaN and False for others.
is_null = df.isnull()
print(is_null)

# we use notnull() function this function return dataframe of Boolean values which are False for NaN values.
not_null = df.notnull()
print(not_null)



# Filling missing values using fillna(), replace() and interpolate()
# In order to fill null values in a datasets, we use fillna(), replace() and interpolate() function
# these function replace NaN values with some value of their own.

# Interpolate() function is basically used to fill NA values in the dataframe


# Filling null values with a single value

df = df.fillna(0)
print(df)

# Filling null values with the previous ones
#   df.fillna(method ='pad')

# Filling null value with the next ones
#    df.fillna(method ='bfill')

# Filling a null values using replace() method ..
df.replace(to_replace='NA', value=100)


# Dropping missing values using dropna()
# we used dropna() function this function drop Rows/Columns of datasets with Null values in different ways.

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

print(df)
# Dropping rows with at least 1 null value.
#df = df.dropna()
#print(df)


#  Dropping rows if all values in that row are missing.

df = df.dropna(how='all')
print(df)

# Dropping columns with at least 1 null value.

#df = df.dropna(axis=1)
#print(df)

# Dropping Rows with at least 1 null value in CSV file
new_data = df.dropna(axis=0, how='any')
print(new_data)

