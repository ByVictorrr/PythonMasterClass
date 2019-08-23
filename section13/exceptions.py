def factorial(n):
	# n! can be defined as n * (n-1)
	""" calculates n! recursively """
	if n <= 1:
		return 1
	else:
		#print(n/0)
		return n * factorial(n-1)

try:
	print(factorial(900))
except (RecursionError, OverflowError): # multiple exeptions 
	print("This program cannot calculates factorial that large")
#except ZeroDivisionError:
	#print("This program divides something by zero")

print("Program terminating")


