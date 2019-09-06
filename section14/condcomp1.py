
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
#meals = [] 
#for meal in menu:
#    if "spam" not in meal:
#        print(meal)
#		meals.append(meal)
#	else:
#		meals.append("a meal was skipped")
#
## iusing conditonal expression
#meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
#
## condtional expressions
#x = 12
#expression = "Twelve" if x == 12 else "unknown"

for meal in menu:
	print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")

