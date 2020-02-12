starCount = 60
line1 = "*" * starCount
line3 = "*" * starCount
name = input("What is your name? ")
spaceCount = starCount - 2 - len(name)
space = spaceCount / 2
space1 = " " * int(space)

if len(name)%2 == 1:
    space2 = space1 + " "
else:
    space2 = space1

print(line1)
print("*" + space1 + name + space2 + "*")
print(line3)
