def create_acc(basename, num, numsize) :
    acc = basename + str(num).zfill(numsize)

    line = "NET USER " + acc + " * /ADD"
    print(line)
    write_batch_line(line)


def create_batchfile(filename):
    global file
    file = open(filename, "w")

def close_batchfile():
    file.close()

def write_batch_line(line):
    file.write(line + "\n")

#----------------------------------------------------------

create_batchfile(r"c:\temp\createaccs.bat")


for i in range(1,101):
    create_acc(num=i, numsize=3, basename="testacc")

close_batchfile()
    # solution 1
    #num = str(i)
    #if i < 10:
    #   num = "0" + num
    #if i < 100:
    #   num = "0" + num
    # acc = "testacc" + num
    # cmd = "NET USER " + acc + " * /ADD"
    # print(cmd)


    # solution 2: zfill
    #num = str(i).zfill(3)
    #acc = "testacc" + num
    #cmd = "NET USER " + acc + " * /ADD"
    #print(cmd)