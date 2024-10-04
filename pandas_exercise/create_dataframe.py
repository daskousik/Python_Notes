# Python Pandas DataFrame.....

# Pandas DataFrame is two-dimensional size-mutable,
# potentially heterogeneous tabular data structure with labeled axes (rows and columns).
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

# Pandas DataFrame consists of three principal components, the data, rows, and columns...


# Creating a Pandas DataFrame....
# In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage,
# storage can be SQL Database, CSV file, and Excel file.

# Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc.

# Creating a dataframe using List:----
# DataFrame can be created using a single list or a list of lists.

import pandas as pd
# # list of strings
l = ['Ram', 'Shyam', 'Jadhuuuuuu','abcdfeeeeeeeeeeeeee']

# # Calling DataFrame constructor on list
df = pd.DataFrame(l)
print(df)

# ======================================================================================================================
# Creating DataFrame from dict of ndarray/lists:--------------------
# To create DataFrame from dict of narray/list, all the narray must be of same length.
# If index is passed then the length index should be equal to the length of arrays.
# If no index is passed, then by default, index will be range(n) where n is the array length.

dict = {'Name':['Akash','Rakesh', 'Rajesh', 'Rashon'],
        'Age':[25, 21, 30, 40],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']
        }

df2 = pd.DataFrame(dict)
print(df2)

# ======================================================================================================================

# Dealing with Rows and Columns: ------------------------
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.

# Column Selection:---------
# In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.

# selecting a single column by their culumn name
print(df2['Name'])

# For selecting multiple column we need to pass list of columns wants select.

print(df2[['Name', 'Qualification']])

# =====================================================================================================================
# Row Selection:-----------
# Pandas provide a unique method to retrieve rows from a Data frame.
# DataFrame.loc[] method is used to retrieve rows from Pandas DataFrame.

#  Rows can also be selected by passing integer location to an iloc[] function.
df3 = pd.DataFrame(dict, index=['one', 'two','three', 'four'])
print(df3)

# # Retrieving row by loc method
print(df3.loc['one'])
print(df3.loc['four'])

# Pandas head() method is used to return top n (5 by default) rows of a data frame or series.
print(df3.head(n=2))

# Pandas tail() method is used to return bottom n (5 by default) rows of a data frame or series.
print(df3.tail(n =1))

# DataFrame rows and columns data structure can be converted to NumPy ndarray with the help of the DataFrame.to_numpy() method...
arr = df3.to_numpy()
print(arr)


# Here we want to convert a particular column into numpy array.

arr2 = df3[['Name', 'Qualification']].to_numpy()
print(arr2)

# Convert Age column in float data type using to_numpy
print(df3['Age'].to_numpy(dtype= 'float64'))


# Pandas Series.as_matrix() function is used to convert the given series or dataframe object
# to Numpy-array representation.

