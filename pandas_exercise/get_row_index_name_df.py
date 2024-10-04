#How to get rows/index names in Pandas dataframe

# Import pandas module....
import pandas as pd

# Load data into Pandas DataFrame using pandas..
df = pd.read_csv('nba.csv')

# Print top 10 DataFrame
print(df.head(10))

# Get Name column first records..
print(df['Name'][0])

# Iterate through each name
for name in df.Name:
    if name == 'Jonas Jerebko':
        pass

# Get top 5 rows in DataFrame using head() method and store in new variable..
df_top = df.head()
print(df_top)

# [5 rows x 9 columns]
# [0, 1, 2, 3, 4]
print((df_top.index.values.tolist()))

for row in df.index:
    print(row, end=' ')


# Get Empty DataFraame , list of columns name and empty index list.
df_top = df.head(0)
print(df_top)

# Get first row with column name....
df_top = df.head(1)
print(df_top)

# Get Index
print(df.index[1])

