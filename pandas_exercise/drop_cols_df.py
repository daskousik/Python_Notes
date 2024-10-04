# How to drop one or multiple columns in Pandas Dataframe.....
import pandas as pd
df = pd.read_csv('nba.csv', index_col='Name')

print(df.head())

# Drop multiple columns
df.drop(['Height', 'Weight'],axis=1, inplace=True)
print(df.head())


# # We can remove three columns as index base
# df.drop(df.columns[[0, 4, 2]], axis=1, inplace=True)

# # Remove all columns between column index 1 to 3
# df.drop(df.iloc[:, 1:3], inplace=True, axis=1)

#
# Remove all columns between column name 'B' to 'D'
#df.drop(df.loc[:, 'B':'D'].columns, axis=1)

for col in df.columns:
    print(col)

