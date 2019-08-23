import sqlite3

conn = sqlite3.connect("contacts.sqlite")
name = input("enter your name: ")
# LIKE - lets you search for lowercase or uppercase name
# (name,) - tupil containg one element
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
	print(row)

conn.close()
