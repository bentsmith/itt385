import tarfile


filename = input("Enter a TAR filename: ")


if(filename.endswith(".gz")):
    mode = "r:gs"
else:
    mode = "r"


tf = tarfile.open(filename,mode)

print("Here are the files within the TAR file: ")

for f in tf.getnames():
    print("...", f)

innername = input("enter the name of a single file within the TAR file: ")

f = tf.extractfile(innername)