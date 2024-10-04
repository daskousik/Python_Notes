# Apply function to every row in a Pandas DataFrame
# There are various ways to Perform element-wise operations on DataFrame columns.
# here we are discussing some examples for Perform element-wise operations on DataFrame columns those are following.
#
#1.  Applying User-Defined Function to Every Row of Pandas DataFrame.
#2.  Apply Lambda to Every Row of DataFrame
#3.  Apply NumPy.sum() to Every Row
#4.  Normalizing DataFrame Column Values Using Custom Function in Pandas
#5.  Applying Range Generation Function to DataFrame Rows in Pandas

#  One can use apply() function to apply a function to every row in a given data frame.
#1.  Applying User-Defined Function to Every Row of Pandas DataFrame
import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head(10))


