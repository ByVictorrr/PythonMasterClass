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
* Pros: loop control variable with same name isnt modified 
* Comprehnsions - can be conditional



