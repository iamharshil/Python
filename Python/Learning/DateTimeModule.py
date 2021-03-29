import datetime
import pytz

d = datetime
today = d.date.today()
print(today)

birthday = d.date(2001, 10, 11)
print((birthday))

day_since_birth = (today - birthday).days
print(day_since_birth)

tdelta = d.timedelta(days=10)
print(today+tdelta)

print(today.weekday())
print(today.weekday())

print(d.time(7,2,20,15))
"""
there is 
d.date(y, m, d)
d.time(h, m, s, ms)
d.datetime(y, m, d, h, m , s, ms)
"""


#add 10 hour to current hours
hour_delta = d.timedelta(hours=10)
print(d.datetime.now()+ hour_delta)

datetime_today = d.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
for tz in pytz.all_timezones:
  print(tz)

#formatting 2019-03-9 --> march 9, 2019
print(datetime_pacific.strftime('%B %d, %Y'))
#march 09, 2019 --> datetime(2019,03,09)
datetime_thing = d.datetime.strptime('march 09, 2019', '%B %d, %Y')
print(repr(datetime_thing))

#see github.com/kennethreitz/maya


#04:03:05