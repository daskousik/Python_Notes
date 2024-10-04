# Add a row at top in pandas DataFrame
import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head())

#  Adding row at the top of given dataframe by concatenating the old dataframe with new one. ...
new_row = pd.DataFrame({'Name':'Kousik', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999}, index=[0])

df = pd.concat([new_row, df])
print(df.head())

# Adding row at the top of given dataframe by concatenating the old dataframe with new one.

df = pd.concat([new_row,df[:]])
print(df.head())


# Adding row at the top of given dataframe by concatenating the old dataframe with new one using df.ix[] method.


