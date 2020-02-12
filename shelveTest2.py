import shelve
import pickle

db = shelve.open(r"c:\Users\Labuser\Desktop\offices.db")

m = { "first" : "mark", "last": "monnin", "email" : "mark.monnin@maine.edu"}

db ["monnin"] = pickle.dumps(m)

mm = pickle.loads(db["monnin"])

db.close()