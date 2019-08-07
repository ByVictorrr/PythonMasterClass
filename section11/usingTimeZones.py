import pytz
import datetime


country = "America/Los_Angeles"
tz_to_display = pytz.timezone(country)
print("=="*20)
print(tz_to_display)

print("=="*20)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time is {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))
