# un ordered
fruit = {"orange": "a sweet, orange citris fuit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citris fruit",
        "grape": "a small, sweet fruit growing bunch",
        "lime": "a sour, green citris fuit"
}

#print(fruit)

veg = {"cabage": "every child favorite",
        "sprouts":"mm lovely",
        "spinach": "can i have more "
}

#print(veg)

veg.update(fruit)
print(veg)


nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)