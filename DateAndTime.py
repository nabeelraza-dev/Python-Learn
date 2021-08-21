import time

import calendar

tick = time.time()
print(tick)

print(time.localtime(tick))

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)