import calendar
calendar.setfirstweekday(calendar.SATURDAY)
# print(calendar.weekheader(3))
# print(calendar.isleap(2000))
leeps = calendar.leapdays(2000,2022)
# print(leeps)

# Day 2 
january = calendar.month(2022, 3, 2, 1)
# print(january)
thisyear = calendar.calendar(2022, 2, 2, 3, 4)
# print(thisyear)

dayoftheweek = calendar.weekday(2022, 11, 7)
# print(dayoftheweek)

numdays = calendar.monthrange(2022, 12)
print(numdays)
weekaday = calendar.weekday(2022, 12, 1)
print(weekaday)