from datetime import datetime, date
import sys

def what_day_is_it(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return(days[day])

uber = dict()

tmp = sys.argv
f_read = open(tmp[len(tmp)-2], "rt")
f_write = open(tmp[len(tmp)-1], "wt")

for line in f_read:
    line = line.strip()
    tmp = line.split(",")
    d = tmp[1].split("/")
    dates = what_day_is_it(date(int(d[2]), int(d[0]), int(d[1])))

    result = tmp[0] + ',' + dates
    if result in uber:
        num1 = uber[result].split(",")
        num1[0] = int(num1[0]) + int(tmp[2])
        num1[1] = int(num1[1]) + int(tmp[3])
        uber[result] = str(num1[0]) + "," + str(num1[1])
    else:
        uber[result] = str(tmp[2]) + "," + str(tmp[3])

for k in uber:
    f_write.write(k + " " + uber[k]+"\n")

f_read.close()
f_write.close()
