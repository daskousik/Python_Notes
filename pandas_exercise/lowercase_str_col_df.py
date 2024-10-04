# How to lowercase strings in a column in Pandas dataframe

import pandas as pd

df = pd.read_csv('nba.csv')
df = df.fillna('0')
print(df.head(10))

# Using str function with  dataframe column make lower all value for this column.
df['Name'] = df['Name'].str.lower()  # Or upper case we can use upper() function....
print(df.head(10))


df['College'] = df['College'].apply(lambda x : x.lower().title())  # capitalize()

print(df.head(10))

df['Team'] = df['Team'].apply(lambda x: x.upper())
print(df.head(10))

# Get n-largest values from a particular column in Pandas DataFrame
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df = df.nlargest(10, ['Salary'])
print(df)

# N number of smallest value to find use nsmallest()