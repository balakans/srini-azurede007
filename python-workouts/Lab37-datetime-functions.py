from datetime import datetime, date, time




s = "Inceptez"

print("Length of Inceptez:",len(s))
print("Upper case of Inceptez",s.upper())

print("========================")
#Create current date/time

now = datetime.now()
print(now)  # Full datetime


today = date.today()
print(today)  # Date only



print("========================")

#Create specific date or time
d = date(2024, 8, 5)
t = time(10, 30, 45)
dt = datetime(2024, 8, 5, 12, 30, 45)

print(d)
print(t)
print(dt)

print("========================")
print("Year:",d.year)
print("Month:",d.month)
print("Day:",d.day)


print("Hour:",dt.hour)
print("Minute:",dt.minute)


#Add days, weeks, hours, minutes, etc.

from datetime import timedelta

today = datetime.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)
plus_5_days = today + timedelta(days=5)
minus_2_hours = today - timedelta(hours=2)

print("========================")

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
print("Next Month:",next_month)
print("Next Week:", next_week)
print("5 Days Later:", plus_5_days)
print("2 Hours Earlier:", minus_2_hours)


print("========================")
#Date Difference
d1 = date(2025, 8, 5)

d2 = date(2025, 7, 1)

diff = d1 - d2
print("Date Difference:",diff.days)

print("========================")

#Format datetime using strftime
dt1 = now.strftime('%Y-%m-%d %H:%M:%S')
print(dt1)

#2025/08/05
dt1 = now.strftime('%Y/%m/%d')
print(dt1)

#05/08/2025
dt1 = now.strftime('%d/%m/%Y')
print(dt1)

print("========================")
# Parse string to datetime
dt1 = datetime.strptime('2025-08-04', '%Y-%m-%d')
print(dt1)


strdate = "05/06/2025"

#output = 2025-06-05

dtf1 = datetime.strptime(strdate,"%d/%m/%Y")
print(dtf1)
strf1 = dtf1.strftime("%Y-%m-%d")
print(strf1)

