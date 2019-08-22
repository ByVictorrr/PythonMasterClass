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
		self._wing = Wing(.9)

	def walk(self):
		print("Waddle, waddle pen")
	
	def swim(self):
		print("come in its chilly in south")
	
	def quack(self):
		print("quack are you 'avin' a lar? im a penguin")

	def fly(self):
		self._wing.fly()


# shows polymorphism
#def duck_test(duck):
#	duck.walk()
#	duck.swim()
#	duck.quack()


if __name__ == "__main__":
	donald = Duck()
	donald.fly()
#	duck_test(donald)
#	penguin = Penguin()
#	duck_test(penguin)

