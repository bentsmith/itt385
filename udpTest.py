#UDP program

import socket

sock = socket.socket(type=socket.SOCK_DGRAM)

# we are going to use broadcasts, so we have to do an extra step
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# need to set out port, in this case UDP port 12345 (on all interfaces)
sock.bind( ("", 12345) )

# get ready to transmit
line = "Can't Kill a God\n"
line = line.encode('utf-8')

# send it to host 255.255.255.255 and UDP port 12345
# aka to all hosts and interfaces

sock.sendto(line, ("255.255.255.255", 12345))

# now wait for others to transmit some data to me
while True:
    (data, addr) = sock.recvfrom(10240) #bigish buffer

    #decode from bytes()
    data = data.decode('utf-8')

    print( str(addr), "said", data)