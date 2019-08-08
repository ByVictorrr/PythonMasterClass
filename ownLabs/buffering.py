# we need buffering for io operations that are a lot of GB's

output = open("exampleOutput.txt", "a")

# 2  million bytes were going to buffer
with open("buffering.py", "a", buffering=2000000) as f:
	for line in f:
		saveLine = line.replace("Plugin", "")
		output.write(saveLine)

output.close()



