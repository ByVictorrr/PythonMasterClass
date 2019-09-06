
#def print_backwards(*args, file=None):
def print_backwards(*args, **kwargs):
	print(kwargs)
	# kwargs.pop("end", None)
	for word in args[::-1]:
		print(word[::-1], **kwargs)

with open("backwards.txt", "w") as backwards:
	print_backwards("hello", "take", "me", "to", "your", "leader", file=backwards)
	print("Another String")



print("hello", "take", "me", "to", "your", "leader", end='\n', sep='|')
print_backwards("hello", "take", "me", "to", "your", "leader", end='\n', sep='|')






# kwargs - key word args
# ** - unpacks a dictionary (instead of defining default paramets as function parms)k
#scoopes up keyword parametes and there values in **kwargs (type(kwargs)) = dic



