import pg8000
import getpass

passwd = getpass.getpass("Enter password for 'user':")

conn = pg8000.connect("user", host="172.22.80.39", password=passwd, database="itt385", ssl=True)


first = input("First Name?")
last = input("Last Name?")
state = input("State?")
city = input("City/Town?")

cur = conn.cursor()

# INSERT INTO
cur.execute("INSERT INTO contacts (first_name, last_name, state, city) " + "VALUES (%s,%s,%s,%s);", args=[first,last,state,city] )

#
cur.execute("SELECT first_name, last_name FROM contacts WHERE state = %s:", args=[state])

for row in cur.fetchall():
    print(row[0], row[1])
