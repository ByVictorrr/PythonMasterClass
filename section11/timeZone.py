import time

print("the epoch on this sytem starts at ", time.strftime("%c", time.gmtime(0)))
print("current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if(time.daylight != 0):
    print("\tDaylight saving time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])
    
    print("local time is " + time.strftime("%Y-%m-%d %H:%M:%S", tuple(time.localtime())))
    print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", tuple(time.gmtime())))
    