# Combining multiple columns in Pandas groupby with dictionary.....

import pandas as pd

# Create dict data
d = {'id':['1', '2', '3'],
     'Column 1.1':[14, 15, 16],
     'Column 1.2':[10, 10, 10],
     'Column 1.3':[1, 4, 5],
     'Column 2.1':[1, 2, 3],
     'Column 2.2':[10, 10, 10]
     }

# Covert dict into a dataframe
df = pd.DataFrame(d)
print(df)

#Set dataframe index as a column id
df.set_index('id', inplace=True)
print(df)

# Creating the groupby dictionary
grouped_dict = {
    'Column 1.1': 'Column 1',
'Column 1.2': 'Column 1',
'Column 1.3': 'Column 1',
    'Column 2.1': 'Column 2',
'Column 2.2': 'Column 2'

}

df = df.groupby(grouped_dict, axis=1).min()

print(df)