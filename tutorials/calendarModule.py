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
# print(numdays)
weekaday = calendar.weekday(2022, 12, 1)
# print(weekaday)

weeksInMatrx = calendar.monthcalendar(2022, 12)
# print(weeksInMatrx)
# for i in weeksInMatrx:
#     print(i)

# Change the default setting

c = calendar.Calendar()
# for i in c.iterweekdays():
#     print(i, end=' ')

m = calendar.Calendar()
# for i in m.itermonthdates(2022, 11):
#     print(i)
# print(calendar.monthrange(2022, 11))

# for i in m.itermonthdays2(2022, 11):
#     print(i)

mntdates = calendar.Calendar()
# for i in mntdates.monthdatescalendar(2022, 11):
#     print(i)

# for i in c.monthdays2calendar(2022, 11):
#     print(i)

# for i in c.monthdayscalendar(2022, 11):
#     print(i)


c = calendar.TextCalendar()

# print(c.formatmonth(2022, 11))
# c.prmonth(2022, 11)
# print(c.formatyear(2022))
# print(c.formatday(1, 0, 2))
# for name in calendar.month_name:
#     print(name)


from datetime import date, datetime

# print(date.strftime(date("08-05-2015"), ("%Y,%d,%m")))
print(datetime.strptime("08,05,2015", "%m,%d,%Y"))

def mtch(argument):
    match argument:
        case 0:
            return 'Monday'
        case 1:
            return 'Tuesday'
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case default:
            return "Something"
print(mtch(wkday))
