# Python | Pandas Working With Text Data......................
# Series and Indexes are equipped with a set of string processing methods that make it easy to operate
# on each element of the array. Perhaps most importantly, these methods exclude missing/NA values automatically.
# These are accessed via the str attribute and
# generally, have names matching the equivalent (scalar) built-in string methods.

import  pandas as pd

df = pd.read_csv('nba.csv')
print(df)

# # converting and overwriting values in column 'Name'
df['Name'] = df['Name'].str.lower()
print(df.head(3))

df['Team'] = df['Team'].str.upper()
print(df.head(3))


# Splitting and Replacing a Data...............................................................
# Pandas str.split() method can be applied to a whole series.
# .str has to be prefixed every time before calling this method to differentiate it from the Python’s default function

df.dropna(inplace=True)
print(df)

df1 = df['Team'].str.split('T', n = 1, expand = True)
print(df1)

df1.columns = ['Team{}'.format(x+1) for x in df1.columns]
print(df1)

df = df.join(df1)
print(df)


df['Name'] = df['Name'].str.replace('a', 'A')
print(df)


# Concatenation of Data.............................................................................

df['Name'] = df['Name'].str.cat(df['Team1'], sep=', ')

print(df)

