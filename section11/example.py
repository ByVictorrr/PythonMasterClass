import shelve
# so what is in std lib
#print(dir())

#print(dir(__builtins__))
#for m in dir(__builtins__):
#    print(m)

#print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != "-":
        print(obj)
