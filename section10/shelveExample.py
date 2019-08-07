import shelve

# with shelve.open("shelfTest") as fruit:
#     fruit["orange"] = "a sweet orange, citrus fruit"
#     fruit["apple"] = "good for making cider"
#     fruit["lemon"] = "sour yellow citris fruit"
#     fruit["grape"] = "a small, sweet fruit grwoing in bunches"
#     fruit["lime"] = "green fruit thats sour"

#     print(fruit['lemon'])
#     print(fruit['grape'])
#     print(fruit)

# leaving shelf open
fruit = shelve.open("shelfTest")
fruit["orange"] = "a sweet orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "sour yellow citris fruit"
fruit["grape"] = "a small, sweet fruit grwoing in bunches"
fruit["lime"] = "green fruit thats sour"
# print(fruit['lemon'])
# print(fruit['grape'])
# print(fruit)

# while True:
#     dict_key = input("input a fruit: ")
#     if(dict_key == "quit"):
#         break
#     description = fruit.get(dict_key, "we dont have a " + dict_key)
#     print(description)

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

print("="*40)

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()