# sorting a list of tuples using Lambda
list1 = [('eggs', 5.25), ('honey', 9.70)]
list1.sort(key=lambda x: x[1])


# sortin a list of Dictionaries using lambdas

import pprint as pp
list1 = [{'make': 'ford', 'model': 'focus', 'year': 2013},{'make': 'Tesla', 'model': 't-series', 'year': 2018}]

#list2 = sorted(list1, key = lambda )



# Filtering a list of Integers using Lambda
list1 = [1,2,3,4]
list2 = list(filter(lambda x: x%2==0, list1))


# Lambda Fucntoin on a List using Map
list1 = [1,2,3,4]
list2 = list(map(lambda x: x ** 2, list1))


# Lambda conditionals - returning a boolean


# Passing a lambda to a function parmater

list_val = [1,3,2,4]
def do_something(f, vals):
	for i in range(0, len(vals)-1):
		if f(vals[i+1], vals[i]) == -1: # if prev is smaller then cur
			temp = vals[i+1]
			vals[i+1] = vals[i]
			vals[i] = temp
	

do_something(lambda cur, prev: 1 if cur-prev > 0 else -1 if cur-prev < 0 else 0, list_val)

print(list_val)


