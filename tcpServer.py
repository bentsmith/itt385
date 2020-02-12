# simple tcp server

import socket

# TCP default
master_socket = socket.socket()

# bind server to a port number & interfaces. ip of interfaces, tcp port
master_socket.bind(("", 12345))

# start listening for connections. the number is the "backlog"
master_socket.listen(5)



# loop forever
while True:
    # wait for a connection request, accept, send data, close, and repeat

    print("Waiting for a connection...")
    # create secondary socket and accept connection request. remote_address is tuple of where the socket is from

    (connection, remote_address) = master_socket.accept()

    # decode tuple
    (host, port) = remote_address

    print("Connection from host", host, "and tcp port", port)

    # send data
    b_str = b"Hello\n"
    connection.sendall(b_str)

    #close connection
    connection.close()

