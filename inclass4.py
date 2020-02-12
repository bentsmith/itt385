#this program covers reading in text files

def method1():
    infile = open(r"c:\temp\threelines.txt", "r")

    # read all in a single step
    s = infile.read()
    print(s, end="")

    infile.close()


def method2():
    infile = open("c:\\temp\\threelines.txt", "r")

    s = infile.readline()
    print(s, end="")

    s = infile.readline()
    print(s, end="")

    infile.close()


def method3():
    infile = open("c:\\temp\\threelines.txt", "r")

    for s in infile:
        print(s, end="")

    infile.close()