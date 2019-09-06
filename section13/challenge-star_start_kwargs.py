def print_backwards(*args, end='', **kwargs):
	print(kwargs)
	#kwargs.pop('end', None) - removing from dictonary
	for word in args[::-1]:
		print(word[::-1], end=' ', **kwargs)

print_backwards("hello", "take", "me", "to", "your", "leader", end='\n')


# ** - unpacks a dictionary (instead of defining default paramets as function parms)
#		scoopes up keyword parametes and there values in **kwargs (type(kwargs)) = dic



