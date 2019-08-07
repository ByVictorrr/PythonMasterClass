# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

print("time\t",time.get_clock_info("time"))
print("per_counter()\t",time.get_clock_info("perf_counter"))
print("monotomic()\t" ,time.get_clock_info("monotonic"))
print("processtime() \t", time.get_clock_info("process_time"))
    



