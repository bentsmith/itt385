# simple TCP client

import socket

# defaults to TCP, create socket
sock = socket.socket()

# connect the socket, needs address. requires two parenthesis to create a tuple
sock.connect(("172.22.80.39", 17))

#receive data. no need to send since we are just listening
data = sock.recv(1024)

# b converts string to byte
all_data = b""

while len(data) > 0:
    #concatenate chunk data
    all_data = all_data + data
    data = sock.recv(1024)

# convert bytes into string
all_data = all_data.decode('utf-8')

#print string
print(all_data)

#close
sock.close()
