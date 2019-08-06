name = input("What is your name?")
age = int(input("How old are you?"))
if(18 <= age <= 30):
    print("Welcome to the holiday {}".format(name))
else:
    print("sorry we are refusing you, sorry {}".format(name))