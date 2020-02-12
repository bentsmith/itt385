starCount = 60
line1 = "*" * starCount
line3 = "*" * starCount
name = input("What is your name? ")
spaceCount = starCount - 2 - len(name)
spaceCount = spaceCount / 2
space = " " * int(spaceCount)

print(line1)
print("*" + space + name + space + "*")
print(line3)
