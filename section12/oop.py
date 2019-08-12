# a=10
# b=8
# print(a.__abs__())
# print(a+b)

# primitives - are even objects


class Kettle(object):
    
    power_source = "electricity"

    def __init__(self, make,price): # constructor
        self.make = make
        self.price = price
        self.on = False
            
    def switch_on(self):
        self.on = True



kenwood = Kettle("Kenwood", 8.93)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamiliton = Kettle("hamiliton", 823)

print("{} = {}, {} = {}".format(kenwood.make, kenwood.price, hamiliton.make, hamiliton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamiliton))

"""
class : template for creating objects. All objects created using the same class wiill have the same chars
Objects: an instance of a class
Instaniate: create an instance of a class
Method: a function defined in a class
Atrribute: a variable bound to an instance to a class
"""

print(hamiliton.on)
#hamiliton.switch_on()
print(hamiliton.on)


# using type and passing object to switch attribute
Kettle.switch_on(kenwood)
print(kenwood.on)

print("="*80)


kenwood.power = 1.5
print(kenwood.power)
# print(hamiliton.power)
print(Kettle.power_source)
print(kenwood.power_source)
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamiliton.power_source)

# print(Kettle.__dict__)
print(kenwood.__dict__)
# print(hamiliton.__dict__)


#1. python first checks intance namespace __init__ function
#2. python then checks class namepace

