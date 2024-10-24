# Join two text columns into a single column in Pandas
# importing pandas
import pandas as pd

df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'],
                   'First': ['Ganesh', 'Sartaj', 'Anjali']})


print(df)

# Apply '+' operator....
df['Full Name'] = df['First'] + ' ' + df['Last']
#print(df)

# Apply lambda function

df['Full_Name'] = df[['First', 'Last']].apply(lambda x: '_'.join(x), axis=1)

print(df)
