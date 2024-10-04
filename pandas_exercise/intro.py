# Pandas Introduction....
# Pandas is a powerful and open-source Python library..
# The Pandas library is used for data manipulation and analysis.
# Pandas consist of data structures and functions to perform efficient operations on data.

# Pandas is well-suited for working with tabular data, such as spreadsheets or SQL tables.

# The data produced by Pandas is often used as input for plotting functions in Matplotlib,
# statistical analysis in SciPy, and machine learning algorithms in Scikit-learn.

# Python’s Pandas library is the best tool to analyze, clean, and manipulate data.
# Here is a list of things that we can do using Pandas.
#  Data set cleaning, merging, and joining.
#  Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data.
#  Columns can be inserted and deleted from DataFrame and higher-dimensional objects.
#  Powerful group by functionality for performing split-apply-combine operations on data sets.
#  Data Visualization.



# Importing Pandas
import pandas as pd

# Note: Here, pd is referred to as an alias for the Pandas. However, it is not necessary to
#   import the library using the alias, it just helps in writing less code every time a method or property is called.

# Data Structures in Pandas Library..
# Pandas generally provide two data structures for manipulating data. They are:
#
# Series
# DataFrame

# Pandas Series......
# A Pandas Series is a one-dimensional labeled array
# capable of holding data of any type (integer, string, float, Python objects, etc.).
# The axis labels are collectively called indexes.

# The Pandas Series is nothing but a column in an Excel sheet.
# Labels need not be unique but must be of a hashable type.

# The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.

# Creating a Series...........
# Pandas Series is created by loading the datasets
# from existing storage (which can be a SQL database, a CSV file, or an Excel file).
# Pandas Series can be created from lists, dictionaries, scalar values, etc.


data =['a','b', 9, 'd']

ser = pd.Series(data = data)
print(ser)


# Pandas DataFrame........
# Pandas DataFrame is a two-dimensional data structure with labeled axes (rows and columns).

# Creating DataFrame...
# Pandas DataFrame is created by loading the datasets
# from existing storage (which can be a SQL database, a CSV file, or an Excel file).

# Pandas DataFrame can be created from lists, dictionaries, a list of dictionaries, etc.

df = pd.DataFrame() #  empty dataframe
print(df)

data = ['Ram', 'shyam', 'Raghu']
columns = ['name']
df2 = pd.DataFrame(data=data, columns= columns)
print(df2)


