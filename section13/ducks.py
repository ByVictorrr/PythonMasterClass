class Wing(object):
	
	def __init__(self, ratio):
		self.ratio = ratio

	def fly(self):
		if self.ratio > 1:
			print("we can fly")
		elif self.ratio == 1:
			print("this is hard work, but im flying")
		else:
			print("ill just walk")


class Duck(object):

	def __init__(self):
		self._wing = Wing(1.8)

	def walk(self):
		print("Waddle")
	
	def swim(self):
		print("come in waters lovely")
	
	def quack(self):
		print("Quack quack")

	def fly(self):
		self._wing.fly()

class Penguin(object):

	def __init__(self):
		self.fly = self.aviate

	def walk(self):
		print("Waddle, waddle pen")
	
	def swim(self):
		print("come in its chilly in south")
	
	def quack(self):
		print("quack are you 'avin' a lar? im a penguin")
	
	def aviate(self):
		print("I won the lottery and bought a learjet")

class Mallard(Duck):
	pass

class Flock(object):

	def __init__(self):
		self.flock = []

	# Type hinds : duck: Duck
	# Return type : -> returnType
	def add_duck(self, duck: Duck) -> None:
		#if type(duck) is Duck: # check to see if just DUCK type
		#if isinstance(duck, Duck): # for subclass or class of Duck type 
		fly_method = getattr(duck, 'fly', None)
		if callable(fly_method): # check if its a method and not a data attribute
			self.flock.append(duck)
		else:
			raise TypeError("Cannot add duck, are you sure its not a " + str(type(duck).__name__))

	def migrate(self):
		problem = None
		for duck in self.flock:
			try:
				duck.fly()
			except AttributeError as e:
				problem = e
				#print("a penguin cant fly")
				#raise # shows the strack trace
		if problem:
			raise problem


if __name__ == "__main__":
	donald = Duck()
	donald.fly()
#	duck_test(donald)
#	penguin = Penguin()
#	duck_test(penguin)

