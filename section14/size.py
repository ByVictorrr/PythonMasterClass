import sys

# generator object
def my_range(n: int):
	print("my_range starts")
	start = 0
	while start < n:
		print("My_range is returning {}".format(start))
		yield start # yield : the function returns the yielded value then goes in suspened state. Then wakes up where its left off the next time
		start += 1

_ = input("line 12")
big_range = my_range(5)

_ = input("line 15")

#print(next(big_range))

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big range
big_list = []

_ = input("line 22")
for val in big_range:
	_ = input("line 24 - inside loop")
	big_list.append(val)


print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)


print("Looking again ... or not")
for i in big_range:
	print("i is {}".format(i))





