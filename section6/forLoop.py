# for i in range(1,20):
#     print("i is now {}".format(i))

# number = "9,223,372,036,854,775,887"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if (number[i] in "0123456789"):
#         cleanedNumber = cleanedNumber + number[i]

# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))


number = "9,223,372,036,854,775,887"
cleanedNumber = ''
for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    
for i in range(0, 100, 5):
    print("i is {} ".format(i))

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j), end = '\t')
    print("====================")

