# Import necessary modules
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

""" How to create a basic timedelta object? """
timedelta1 = timedelta(days=270, hours=9, minutes=18)
print(timedelta1) # 270 days, 9:18:00

""" How to print the current date and time in python? """

# for reference time use the current time 
time_now = datetime.now() 
print(time_now) # 2022-11-16 19:20:25.958324

"""How to calculate a date in the future in python?"""

# Check what date it will be after time delta
futureDate1 = time_now + timedelta1
print(futureDate1) # 2023-08-14 04:41:45.312839

# What day it will be after 189 days 
futureDate2 = time_now + timedelta(189)
print(futureDate2) # 2023-05-24 19:25:57.427813

"""How to Calculate a Date in the Past in Python?"""

# What day was 189 days ago 
futuredate3 = time_now - timedelta(189)
print(futuredate3) #2022-05-11 19:28:02.826705

""" How to Calculate Time Elapsed or Time Remaining in Python? """
# Create reference date for today and teachers' day 
teachersDay = date(2023, 9, 5)
today = date.today()

# Calculate the number of days to teachers' day 
timeToTD = teachersDay - today
print(f"Teachers' day is {timeToTD.days} days away")

#dt1 = datetime(Sun 10 May 2015 13:54:36 -0700")
#dt2 = datetime('Sun 10 May 2015 13:54:36 -0000')

# dtplus = dt1 + dt2
# print(dt1)

# Importing dateparser Module 
import dateparser

dt1 = dateparser.parse("Sun 10 May 2015 13:54:36 -0700")
dt2 = dateparser.parse("Sun 10 May 2015 13:54:36 -0000")
diff_hrs = dt1 - dt2
#secs = datetime.timedelta(seconds = diff_hrs*60*60).total_seconds() 
print(diff_hrs.total_seconds())

def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff_hrs = dt1 - dt2
    return diff_hrs.total_seconds()

secs = time_delta("Sun 10 May 2015 13:54:36 -0700","Sun 10 May 2015 13:54:36 -0000")
print(secs)
