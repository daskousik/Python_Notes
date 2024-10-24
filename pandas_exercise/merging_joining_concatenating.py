# Python | Pandas Merging, Joining, and Concatenating............

# In Dataframe df.merge(),df.join(), and df.concat() methods help in joining, merging and concating different dataframe.

# Concatenating DataFrame.....
# In order to concat dataframe, we use concat() function which helps in concatenating a dataframe.

# We can concat a dataframe in many different ways, they are:

# Concatenating DataFrame using .concat()
# Concatenating DataFrame by setting logic on axes
# Concatenating DataFrame using .append()
# Concatenating DataFrame by ignoring indexes
# Concatenating DataFrame with group keys
# Concatenating with mixed ndims

#1 # Concatenating DataFrame using .concat()............................................
# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])
print(df1)

# Convert the dictionary into DataFrame
df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])
print()
print(df2)

# Now we apply .concat function in order to concat two dataframe.


frames = [df1, df2]
df_concat =pd.concat(frames)
# we have created two dataframe after concatenating we get one dataframe.
print(df_concat)


# Concatenating DataFrame by setting logic on axes :
df_res = pd.concat([df1, df2], axis=1, join='inner')

print(df_res)

# Now we used a specific index, as passed to the join_axes argument
# res3 = pd.concat([df, df1], axis=1, join_axes=[df.index])

# Concatenating DataFrame by ignoring indexes :
# res = pd.concat([df, df1], ignore_index=True)

# ======================================================================================================================

# Merging DataFrame...........
# Pandas provide a single function, merge(), as the entry point for all standard database join operations
# between DataFrame objects.

# Define a dictionary containing employee data
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32]}

# Define a dictionary containing employee data
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df3 = pd.DataFrame(data1)

df4 = pd.DataFrame(data2)
print('Dataframe using merge....................')
# Merging a dataframe with one unique key combination
res = pd.merge(df3, df4,how='inner', on='key')
print(res)


# Merging dataframe using multiple join keys.....
# res1 = pd.merge(df, df1, on=['key', 'key1'])

# Merging dataframe using how in an argument:

# # joining string and overwriting
res['Name'] = res['Name'].str.join('-')
print(res)
