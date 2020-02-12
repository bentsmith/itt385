import zipfile

filename = input("Enter zipfile name: ")

zf = zipfile.ZipFile(filename)

print("Here are the files within the .zip file")

for f in zf.namelist():
    print("...", f)

innername = input("Enter name of a single file within the .zip file: ")

f = zf.open(innername)

line1 = f.readline()
line1 = line1.decode('utf-8')

print("The first line of that file is: ")
print(line1)
