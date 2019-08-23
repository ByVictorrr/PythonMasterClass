import sqlite3

# sqlite3 doesnt care what you name your file
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Victor', 6507406691, 'vdelaplainess@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# a list of tupils
print(cursor.fetchall())

for row in cursor:
    print(row)
db.commit()
db.close()

