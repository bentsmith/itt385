import os


start = input("Enter in starting point:")

for (dirname, dirs, files) in os.walk(start):
    print(dirname)

    for f in files:
        print("...", f)
