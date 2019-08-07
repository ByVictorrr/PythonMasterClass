x = int(input("Enter a number to be converted to binary: "))
binary = []
counter = x
num_bits = 0

if(x <= 65535):
    #print x in binary
    while(counter > 0):
       binary.append(str(counter % 2))
       counter //= 2

    print("your number in binary is")
    for i in binary[::-1]:
        print(i, end = '')
else:
    print("enter a number below 65535")

