print(__file__)

numbers = [1,2,3,4,5,6]
number = int(input("please enter num ill tell u its square"))

#squares = [number **2 for number in numbers] # list comprehension

squares = [number **2 for number in range(1,7)] # list comprehension

set_squres = {number **2 for number in numbers} # set comprehnsion

index_pos = numbers.index(number)
print(squares[index_pos])
