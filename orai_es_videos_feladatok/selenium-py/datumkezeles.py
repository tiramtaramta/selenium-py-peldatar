# https://docs.python.org/3/library/datetime.html
# object
#    timedelta
#    tzinfo
#        timezone
#    time
#    date
#        datetime

from datetime import datetime, date, time, timezone
# ha csak a datetime opciót szeretnénk importálni
# egyéb esetben import datetime és később a datetime.afentieközül valami

print(datetime.now(timezone.utc))  # nulla időzóna, de mi inkább gmt+1 zónában vagyunk

# a dátum inmutable ==> azaz nem változtatható

# egyéb lekérdezésekhez már érdemes egy változóba betenni
now_utc = datetime.now(timezone.utc)
print(now_utc)
print(now_utc.date())
print(date(2000, 1, 1))
