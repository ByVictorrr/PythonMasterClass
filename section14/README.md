# Section 14 - Generators and Lambdas

## Generator Object - a special case of an iterator
* can be considered as a range
* save a lot of memory vs iterating over a list 
* when it is assigned it isnt called
* range class acts like an iterable after its called its reset 

### What does yield do? 
* the function returns the yielded value and goes into a suspended state 
* so next time it goes where it is left off


### What is a comprehension in python?
* List comprehnsion:
	* [number **2 for number in numbers if number % 2 = 0]
		*expression | iterator | filter
		*or you can have
			* expression if condition else expression | iterator
* Pros: loop control variable with same name isnt modified 
* Comprehnsions - can be conditional


## Maps
* map(function_addr, iterator)
* it pretty much calls that function on an item in the iterator 
* it returns an iterator

## Filters
* filter(function, iterator)
* if the filter function returns true it passes on that item in the iterator


## The Reduce Function
* It takes a function and a sequence then reduces the sequence to a single value
by calling the function
* import functools
	* functools.reduce(function, iterable)


## Any 
* returns true if the iterable if any are true values not zero or null, ect.

## All
* returns true if all the items in iterable if everything is not zero, null
empty list, ect.
* Edge case: all([]) = True

## Named Tuples
* collections.namedtuples(typename_str)
* extra functionality 
	* using dot notation to acess field
		* name_tuple_var.field

## Lambdas
* short -term function, throwaway function, one line functions
* syntax: (lambda args: expression) 
	* Examples: lambda x: x + 5
	* lambda p: int(p/10) % 10

	
