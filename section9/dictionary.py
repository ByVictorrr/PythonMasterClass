# un ordered
fruit = {"orange": "a sweet, orange citris fuit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citris fruit",
        "grape": "a small, sweet fruit growing bunch",
        "lime": "a sour, green citris fuit"
}

#print(fruit)
# print(fruit["grape"])
# # add new item to dictionary
# fruit["pear"] = "an odd shape apple"
# print(fruit)
# # update an entry
# fruit["pear"] = "a new update "

# # how to see if an entry is in the dictionary
# while True:
#     dic_key = input("please enter a fruit: ")
#     if(dic_key == "quit"):
#         break #     description = fruit.get(dic_key, "we dont have a " + dic_key) #     print("not in dictionary")

# for i in range(10):
#     for snack in fruit:
#         print(snack +  "is " + fruit[snack])
#     print("-" *40)

# for f in  sorted(list(fruit.keys())):
#     print(f + '-' + fruit[f])

# for val in fruit.values():
#     print(val)

#print(fruit)
#print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
