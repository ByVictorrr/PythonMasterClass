burgers = ['beef', 'chicken', 'Spicy bean']
toppings = ["cheese", "egg", "beans", "spam"]

# nested list comprehension
#[(exp) | iteration | 2nd iteration]
meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

#for meals in [(burger, topping) for burger in burgers for topping in toppings]:
#	print(meals)
#
#for burger in burgers:
#	for topping in toppings:
#		print((burger,topping))
#
print()

# [((expr) | iteration)->list comprehension(expression) | iteration]
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
	print(meals)


