import sqlite3

conn = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

#for row in conn.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime, history.amount FROM history  ORDER BY history.time"):
for row in conn.execute("SELECT * FROM localhistory"):
	print(row)

	#utc_time = row[0]
	#local_time = pytz.utc.localize(utc_time).astimezone()

conn.close()
