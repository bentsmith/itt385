import json

js = json.loads('{ "a" : "b", "c" : "d" } ')
print(type(js))

print("---")


js2 = json.loads('[1,3,5,9]')
print(type(js2))

print("---")

# make a dictionary
python1 = {"key1" : "val1", "key2" : "val2", "key3" : 333}
s = json.dumps(python1)
print(s)

print("---")

# make a list

python2 = [2,4,6,8, "hi mom", 10]
s = json.dumps(python2)
print(s)
print("---")


# open big json file
with open(r"c:\Users\labuser\Desktop\data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)