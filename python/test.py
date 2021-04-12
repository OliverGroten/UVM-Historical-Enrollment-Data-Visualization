import mysql.connector

mydb = mysql.connector.connect(
	host="webdb.uvm.edu",
	user="oreckord_reader",
	password="hfDC3mIJGXkG"
)

print(mydb)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
	print(x)
