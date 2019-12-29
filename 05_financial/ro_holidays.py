#!/usr/bin/env python

import sys
import datetime

#
# NOTE: This doesn't take into account days with variable date that always fall on Sunday (Easter or Pentecost) - next Monday after those is also holiday
#

daysOff = [
[1,1], # 1st of January
[2,1], # 2nd of January
[24,1], #24th of January
[1,5], # Labour Day
[1,6], # Child Day
[15,8], # Assumption of Mary
[30,11], # Saint Andrew
[1,12], # Romania's National Day
[25,12], # Christmas
[26,12] # Boxing day
]

totalHolidays=len(daysOff)+4 # Easter and Pentecost add 2+2 more days - 1 on Sunday, one on Monday for each

today = datetime.date.today()
year = today.year

for year in range(year,year+10):
    holidaysInWeekend=2 # by default we start with 2 in weekend (Pentecost and Easter)
    for dayOff in daysOff:
        day = dayOff[0]
        month = dayOff[1]
        d = datetime.date(year,month,day)
        weekday = d.weekday()
        if weekday > 4:
            # that means 5 or 6
            # meaning Saturday or Sunday
            holidaysInWeekend+=1

    print("Year %d has %d (out of %d) holidays falling on weekend." % (year,holidaysInWeekend,totalHolidays))

