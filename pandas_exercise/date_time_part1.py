 # Python | Working with date and time using Pandas.....

# Working with Dates in Pandas.............................................................
# The date class in the DateTime module of Python deals with dates in the Gregorian calendar.
# It accepts three integer arguments: year, month, and day.
import  pandas as pd
from datetime import date
date = date(2024, 10, 15)  # O/P : 2024-10-15
print(date)

# Year, month, and day extraction....
# Retrieve the year, month, and day components from a Timestamp object.

# Creating a Timestamp object..using pandas Timestamp.
timestamp = pd.Timestamp('2024-10-15 22:28:30') # YYYY-MM-DD HH:MM:SS
#timestamp = '2024-10-15 15:28:30' while using this getting error AttributeError: 'str' object has no attribute 'year'
print(timestamp)

# Extracting the year from the Timestamp
year = timestamp.year
print(year)

# Extracting the month from the Timestamp
month = timestamp.month
print(month)

# Extracting the days from the Timestamp
day = timestamp.day
print(day)

# Extracting the hour from Timestamp
hour = timestamp.hour
print(hour)

# Extracting the minute from the Timestamp..
minute = timestamp.minute
print(minute)

# Extracting weekday
weekday = timestamp.weekday()
print(weekday)

# Extracting quater from the Timestamp
quater = timestamp.quarter
print(quater)

# ======================================================================================================================

# Working with Time in Pandas.................................................
# Another class in the DateTime module is called time, which returns a DateTime object
# and takes integer arguments for time intervals up to microseconds:

from datetime import time
t = time(15, 46, 20, 18)  # 15:46:20.000018
print(t)

# Time periods and date offsets

time_period = pd.Period('2024-10-15', freq='M')
print(time_period)

year = time_period.year

# =====================================================================================================================
# Working with Date and Time in Pandas
# Creates dates dataframe  with frequency.........

date_time = pd.date_range('1/1/2024', periods=10, freq='M')
print(date_time)


# create date and time with dataframe......
rng = pd.DataFrame()
rng['date'] = pd.date_range('1/1/2024', periods=72, freq='H') # 2024-01-01 01:00:00

rng['year'] = rng['date'].dt.year
rng['month'] = rng['date'].dt.month
rng['day'] = rng['date'].dt.day
rng['hour'] = rng['date'].dt.hour
rng['minute'] = rng['date'].dt.minute

# Print the dates divided into features
rng.head(3)
print(rng)

# # Convert the Time column to datetime format
# df['Time'] = pd.to_datetime(df.Time)
# # Extract the hour of the day from the 'Time' column
# df['Hour'] = df['Time'].dt.hour
#


# # Get hour detail from time data
# df.Time.dt.hour.head()

# # Get name of each date
# df.Time.dt.weekday_name.head()

#======================================================================================================================

# To get the present time, use Timestamp.now()
time_now = pd.Timestamp.now()
print(time_now)

# # Convert timestamp to datetime

date_time = time_now.to_datetime64()
print(date_time)
