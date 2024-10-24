 # Python | Pandas Timestamp.now
# Pandas Timestamp.now() function returns the current time in the local timezone. It is Equivalent to datetime. now([tz]).
import pandas as pd
current_time = pd.Timestamp.now()
print(current_time)


ts = pd.Timestamp(year=2024, month=10, day=16, tz='US/Central')
print(ts)


# Python | Pandas Timestamp.isoformat..........................
 # Create a Timestamp object in ISO format
time_stamp_obj = pd.Timestamp('2015-06-26 07:35:00', tz='Asia/Kolkata')

# Print the Timestamp object
print("Timestamp Object:", time_stamp_obj)

# Convert the Timestamp object to ISO format
iso_8601 = time_stamp_obj.isoformat()
print("ISO 8601 Format:", iso_8601)

# Pandas Timestamp.date() function return a datetime object with same year, month and day as that of the given Timestamp object.

# return as a datetime object
print(ts.date())



# Python | Pandas.to_datetime()............................................
# Pandas to_datetime() method helps to convert string Date time into Python Date time object.
# is used to convert different data types into datetime objects

# 1 Convert a Pandas String to Datetime....
str_time = '2024-10-16'
dt_obj = pd.to_datetime(str_time)
print(dt_obj)
print(dt_obj.year)


# Convert Pandas Numerical values to Datetime....
timestamp = 1722980
dt_obj = pd.to_datetime(timestamp)
print(dt_obj)


# Convert Pandas Column to DateTime.........

df = pd.read_csv('todatetime.csv')
print(df)

# Converting Date Format using Pandas...

# # Overwriting data after changing the 'Date' format
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())
print(df['Date'].dt.year)



