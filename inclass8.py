# fake atomic operations
import os
# get current count value
cfile = open("c:\\counter.txt")
counter = cfile.readline()
cfile.close()

# use it
print("currently: ", counter)

# update
cint = int(counter)
cint = cint + 1
counter = str(cint)

# update count file iwth new value
cfile = open("c:\\counter.txt", "w")
cfile.write(counter + "/n")
cfile.close()

# delete .old JIC
if os.path.exists("c:\\counter.old"):
    os.unlink("c:\\counter.old")

# save current version as .old
os.link("c:\\counter.txt", "c:\\counter.old")

# replace new file
os.rename("c:\\counter.txt.new", "c:\\counter.txt")