# #ipAddress = input("please enter your ip address: ")
# #print(ipAddress.count("."))
# parrot_list = ["non piin", "no more", "a stiff", "bereft of live"]
# parrot_list.append("A Norweigian blue")
# for state in parrot_list:
#     print("this parrot is " + state)


# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# # makes a bigger list (appending)
# numbers = even + odd
# #numbers.sort()
# numbers_in_order = sorted(numbers)
# if numbers == numbers_in_order:
#     print("The list are equal")
# else:
#     print("The list are not equal")


even = [2, 4, 6, 8]
odd = [1,3,5,7,9]
numbers = [even, odd]

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)

# another_even = list(even)
# # == checks if list has same contents
# print(another_even == even)
# # is check if the vars pointing to same object
# print(another_even is even)
# another_even.sort(reverse=True)
# print(even)


