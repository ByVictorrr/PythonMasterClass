__author__ = "dev"
age = 24
print("my age is " + str(age) + " year")

# replacement field
print("my age is {0} years".format(age))
print("there are {0} in {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(31, "january", "March", "May", "July", "August", "October", "December"))

print("January: {2}\n Febuary {0}\n March: {2}\n April {1}".format(28,30,31))

# old format
print("My age is %d years" % age)
print("My age is %d %s " % (age, "years"))

for i in range(1,12):
    print("No %2d squared is %4d and cubed is %4d" % (i, i ** 2, i**3))
    print("No {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i**3))

print("Pi is approx %12.50f" % (22/7))
print("Pi is approx {0:12.50}".format(22/7))
