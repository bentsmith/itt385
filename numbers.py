a = input("First Number: ")
b = input("Second Number: ")

try:
    a = int(a)
    b = int(b)
    ok = True

except ValueError:
    ok = False

if (ok):
    if(b != 0):
        print(a, "div by", b, "=", a/b)
    else:
        print("no dividing by 0")
else:
    print("Enter a integer number")
