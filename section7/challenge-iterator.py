# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.
num_list = [1,3,4,1,3]
iterator = iter(num_list)
for i in range(0, len(num_list)):
    print(next(iterator))
