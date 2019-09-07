import timeit

text = "what have the romans ever done for us"

def cap_comp():
	capitals = [char.upper() for char in text]
	return capitals

# use map
def cap_map():
	map_capitals = list(map(str.upper, text))
	return map_capitals

def word_comp():
	words = [word.upper() for word in text.split(" ")]
	return words

# use map 
def word_map(): 
	map_words = list(map(str.upper, text.split(" ")))
	return map_words

if __name__ == "__main__":
	print("cap comp function: {}".format(timeit.timeit(cap_comp, number=1000, globals=globals())))
	print("cap map function: {}".format(timeit.timeit(cap_map, number=1000, globals=globals())))
	print("word comp function: {}".format(timeit.timeit(word_comp, number=1000, globals=globals())))
	print("word map function: {}".format(timeit.timeit(word_map, number=1000, globals=globals())))

