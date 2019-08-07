# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)

# for animal in farm_animals:
#     print(animal)

# print("="*40)

# wild_animals = set(["lion", "tiger", "panther", "elephant"])

# for animal in wild_animals:
#     print(animal)

# farm_animals.add("horse")
# farm_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")

# even = set(range(0,40, 2))
# print(even)
# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# even = set(range(0,40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))

# print("---"*40)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)


# even = set(range(0,40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))

# print("="*40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))


# even = set(range(0,40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)

# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error, does nothing
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("item 8 isnt in the set")

# even = set(range(0,40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4,6,9,16,25)
# squares = set(squares_tuple)

# if(squares.issubset(squares_tuple)):
#     print("square is a subset of even")

# if even.issuperset(squares):
#     print("even is a super set of square")


#frozen set - imutable set

even = frozenset(range(0,40, 2))
print(even)

