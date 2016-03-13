import datetime
import time
def stringtoarr (input):
    year = input[0:4]
    month =input[5:7]
    day = input[8:10]
    hour = input[11:13]
    minute = input[14:16]
    second = input[17:19]
    dt = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
    unix = time.mktime(dt.timetuple())
    return unix
