import sys

def validate():
	# validates - an input is a number
	while True:
		try:
			num = int(input("Enter a number"))
			return num
		except ValueError:
			print("enter a valid number")
		except: # gets any exception (wildcard exception)
			print("wild card exception")
		except EOFError:
			sys.exit(1)
		except KeyboardInterrupt:
			sys.exit(2)
		finally:
			print("The finally clause always excutes")

# else - in an if statment
# else - in an try statement goes if sucessfully complete 




if __name__ == "__main__":
	x = validate()
	y = validate()
	try:
		print(x/y)
	except ZeroDivisionError:
		print("Dont divide by zero")
		sys.exit(2)
	else:
		print("divison performed sucessfully")

