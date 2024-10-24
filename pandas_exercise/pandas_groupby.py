# Groupby mainly refers to a process involving one or more of the following steps they are:

# Splitting : It is a process in which we split data into group by applying some conditions on datasets.

# Applying : It is a process in which we apply a function to each group independently

# Combining : It is a process in which we combine different datasets after applying groupby and results into a data structure


# Splitting Data into Groups
#   In order to split the data, we use groupby() function this function is used to split the data into
#   groups based on some criteria.

# There are multiple ways to split data like:
#
#
# obj.groupby(key)
# obj.groupby(key, axis=1)
# obj.groupby([key1, key2])




# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32,
                 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                     'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                           'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

print(df)

# Grouping data with one key:
df = df.groupby('Name')
df2 = df.sum()
print(df2)


# Grouping data with multiple keys :
# In order to groupby multiple key we need to pass list of key.
#df.groupby(['Name', 'Qualification'])

# Group keys are sorted by default using the groupby operation.
#      User can pass sort=False for potential speedups.

# ---------------------------------------------------------------------------------------------------------------------

# Iterating through groups

for name, group in df:
    print(name)
    print(group)
    print()

print(df.get_group('Abhi'))



# ======================================================================================================================
# Grouping Rows in pandas...
# df['Address'].groupby('Name')


