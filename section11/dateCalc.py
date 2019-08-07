#import time

#print(time.gmtime(0))

#print(time.localtime())
#print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("year:", time_here[0], time_here.tm_year)
# print("month:", time_here[1], time_here.tm_mon)
# print("date:", time_here[2], time_here.tm_mday)

import time
from time import process_time as my_timer
import random
# perf_counter = measures time excluding sleep
# time = actual whole time
# monotonic = time cant go backward, rules out day light savings
# process_time = returns time where cpu executing this process


input("please enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()

input("please enter to stop")
end_time = my_timer()
print(end_time)

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("Eneded at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
