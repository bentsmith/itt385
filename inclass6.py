import re

# find things that are in the form 3 letters and space

s = input("Enter a line to check: ")
#pattern = "[A-Z]{3} \d+"
pattern = "\s([A-Z]{3}\s? \d{1,4})\s"

#regular expression search
m = re.search(pattern,s)

# check for matches
if m is not None :
    match = m.group(0)
    print(match)
else:
    print("Nothing was found")