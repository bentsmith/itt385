import pg8000
import getpass
import re

passwd = getpass.getpass("Enter password for 'user':")

conn = pg8000.connect("user", host="172.22.80.39", password=passwd, database="itt385", ssl=True)

state = input("enter state to search")

cur = conn.cursor()
# SELECT first_name, last_name FROM contacts WHERe state = 'ME'; DROP TABLE contacts; --';
state = state.upper()

if re.search("^[A-Z] [A-Z]$", state) is None:
    print("No way!")
# don't do it this way, it opens up a serious security hole
# cur.execute("SELECT first_name, last_name FROM contacts WHERE state = '" + state + "';'")

# do it this way
cur.execute("SELECT first_name, last_name FROM contacts WHERE state = %s;", args=[state])

results = cur.fetchall()

for one_row in results:
    first = one_row[0]
    last = one_row[1]

    print(first,last)


