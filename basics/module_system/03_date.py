from datetime import datetime, date, time
from time import time

current_dateime = datetime.now()
print(current_dateime)
print(type(current_dateime))

print(current_dateime.year)
print(current_dateime.month)
print(current_dateime.day)
print(current_dateime.hour)
print(current_dateime.minute)
print(current_dateime.second)
print(current_dateime.microsecond)

print(datetime(2020, 10, 10))
print(datetime(2020, 10, 10).strftime('%Y. %B %d.'))
print(datetime(2020, 10, 10, 10, 10, 10, 10).isoformat())
print(type(datetime.strptime('2020.10.10.', '%Y.%m.%d.')))
print((datetime(2020, 10, 10) - datetime(2020, 5, 10)).days)
d = date(2020, 10, 10)
print(type(d), d)
t = time(10, 10)
print(type(t), t)
print(datetime.combine(d, t))
