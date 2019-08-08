# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import pytz
import datetime

avail_zones = {
    1: "America/Los_Angeles",
    2: "America/Louisville",
    3: "America/Lower_Princes",
    4: "America/Maceio",
    5: "America/Managua",
    6: "America/Manaus",
    7: "America/Marigot",
    8: "America/Martinique",
    9: "America/Matamoros"
    }
x = 0

while True:
    print("Select one of the timezones below, or 0 to quit")
    for place in sorted(avail_zones):
        print("\t\t{} {}".format(place,avail_zones[place]))

    x = int(input())
    if(x in avail_zones):
        tz_to_display = pytz.timezone(avail_zones[x])
        local_time = datetime.datetime.now(tz=tz_to_display)
        utc_time = datetime.datetime.utcnow()
        print("{}: {}".format(avail_zones[x], local_time))
        print("{}: {}".format("utc time  ", utc_time))
    elif place == 0:
        print("quiting")
        break
    else:
        print("enter a valid zone")




        
