# def python_food():
# 	width = 80
# 	text = "Spam and eggs"
# 	left_margin = (width-len(text)) // 2
# 	print(" " * left_margin, text)

# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
# 	text = ""
# 	for arg in args:
# 		text += str(arg) + sep
# 	left_margin = (80-len(text)) //2
# 	print(" " *left_margin, text, end=end, file=file, flush=flush)


# with open("centred", mode="w") as centered_file:
# 	centre_text("Spam and eggs",file=centered_file)
# 	centre_text("spam, spam and eggs",file=centered_file)
# 	centre_text("spam, spam, spam, spam, and spam", file=centered_file)
# 	centre_text(8, file=centered_file)
# 	centre_text("first", "2nd", "3rd", 8, sep=":", file=centered_file)

def centre_text(*args, sep=' '):
	text = ""
	for arg in args:
		text += str(arg) + sep
	left_margin = (80-len(text)) //2
	return " " * left_margin + text


#with open("centred", mode="w") as centered_file:
print(centre_text("Spam and eggs"))
print(centre_text("spam, spam and eggs"))
print(centre_text("spam, spam, spam, spam, and spam"))
print(centre_text(8))
print(centre_text("first", "2nd", "3rd", 8, sep=":"))








