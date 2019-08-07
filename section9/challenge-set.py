# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.
text_set = set(input("input text: "))
vowels = frozenset("aeiou")

text_set.difference_update(vowels)
list_text = list(text_set)
print(list_text)



