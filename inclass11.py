# small program to send data to a graphite server

import socket
import time

# TCP socket doesn't require any parameters
sock = socket.socket()

# graphite ingress port
sock.connect(( "172.22.80.39", 2003 ))

# graphite data format:
#
# DataPointName Value WhenItHappened
#
# if WhenItHappened = -1 --> "NOW"

val = 1


# create line, convert to bytes(), and transmit
while True:
    line = "itt385.smith.data 100 -1\n"
    line = line.encode("utf-8")
    sock.send(line)

    val = val + 1
    if val > 100:
        val = 1

    time.sleep(10)


# close socket
sock.close()