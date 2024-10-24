# Adding new column to existing DataFrame in Pandas......................

import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())

# Add a new column at last to existing df with default value.
df['Adresss'] = 'Dahiuri'
print(df.head())

# Add a New Column to an Existing Datframe using DataFrame.insert()...
# It gives the freedom to add a column at any position we like and not just at the end.
# It also provides different options for inserting the column values.

df.insert(1, 'New Age', [ age + 2 for age in df['Age']])
print(df.head())


# Add A New Column To An Existing Pandas DataFrame using Dataframe.loc()

# How to create new columns derived from existing columns?
df['Name_College'] = df['Name'] + df['College']
print(df.head())



# Adding More than One columns in Existing Dataframe

weight = df['Weight']
age = df['Age']
new_data = {'New_Weight': weight, 'New_Age': age}
df = df.assign(**new_data)
print(df.head())


