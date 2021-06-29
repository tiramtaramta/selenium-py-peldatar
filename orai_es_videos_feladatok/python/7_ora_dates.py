######## DATETIME #############

import datetime  # ha így importáljuk, akkor datetime.datetime.now()
datetime_object = datetime.datetime.now()
print(datetime_object)  # (év, hónap,nap, óra, perc, másordperc, ezred másodperc)


from datetime import datetime  # ha így importáljuk be, akkor elég csak a datetime.now()
dt = datetime.now()  # (év, hónap,nap, óra, perc, másordperc, ezred másodperc)
print(dt)

from datetime import datetime, timezone
time_zone = datetime.now(timezone.utc)  # UTC timezone szerinti idő.
print(time_zone)

from datetime import date  # importáljuk a date-et a datetime-ból
dd = date.today()  # év-hónap-nap.
print("Current date:", dd)

# tudunk kreálni egy dátumot
my_date = date(1989, 1, 1)  # szigorúan 1, 1 (nem lehet 01, 01)
print(my_date)

# tudunk kreálni egy datetime-ot
from datetime import datetime
my_datetime = datetime(2017, 11, 28, 23, 55, 59)  # datetime(year, month, day, hour, minute, second)
print(type(my_datetime))
print(my_datetime)
# a kreált datetime részben is ki tudjuk nyomtatni
print("year =", my_datetime.year)
print("month =", my_datetime.month)
print("hour =", my_datetime.hour)
print("minute =", my_datetime.minute)

# a date importjával lekérhető a nap és egy változóba helyezve, kiíratható az év, hónap, nap
from datetime import date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


##### Format DATE  https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime
current = datetime.now()  # dátum és idő
print(current)

# .strftime szerkezetek
year = current.strftime("%Y")
print("year:", year)

month = current.strftime("%m")
print("month:", month)

day = current.strftime("%d")
print("day:", day)

time = current.strftime("%H:%M:%S")
print("time:", time)

date_time = current.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)