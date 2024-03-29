import sqlite3

# sqlite3 doesnt care what you name your file
db = sqlite3.connect("contacts.sqlite")

new_email = "anotherupdate@email.com"
phone = input("Please enter the phone number: ")

#update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
# parameter subsistution - allows you to check for safety
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"

print(update_sql)
update_cursor = db.cursor()
# execute script is used for running more than one statment in a call

update_cursor.execute(update_sql, (new_email, phone))

print("{} rows updated".format(update_cursor.rowcount))

print("Are connections the same {}".format(update_cursor.connection == db))

update_cursor.connection.commit()

update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("="*20)

db.close()
