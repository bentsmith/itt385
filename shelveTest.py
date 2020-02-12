import shelve


db = shelve.open(r"c:\Users\Labuser\Desktop\simple-db.db")

db["key1"] = "value1"

key = input("Enter a new key:")
val = input("Enter a value for that key:")

db[key] = val

for k in db.keys():
    print("Key %s = %s" % (k, db[k]))

db.close()