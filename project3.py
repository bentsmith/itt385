# Ben Smith Project 3
# This program creates a TCP socket to listen for HTTP requests from an Excel spreadsheet.
# It then takes the request and analyzes the data against a text file that has all the zip codes in the US
# The program then crafts a packet and sends it back to the excel spreadsheet with the location of that zip
# aka it takes input for a zip code then converts it to a town and state. really complicated google...

import socket
import re

run = True

# mark what is this RegEx?? I was stuck on this for so long until Trina helped me.
# Specifically these two lines below. I strongly dislike RegEx
regEx = "\\/zip\\/(\\d{5})"
location = "HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n{}\r\n"

# create the socket and listen on port :8080
sock = socket.socket()
sock.bind(("", 8080))
sock.listen(5)

print("Socket Started... Waiting for Connection")

# continuously run until excel closes
while run == True:

    # clear variables for every new connection

    packet = ""
    zip = ""
    town_state = ""
    # accept connection and format into
    (conn, rem_addr) = sock.accept()

    # receive data from excel and decode from byte
    excel_data = conn.recv(1024)
    print("Connection Received from:", rem_addr, "\n")
    excel_data = excel_data.decode("utf-8")

    # use re.search to look for zip code matches from excel data
    match = re.search(regEx, excel_data)

    # if statement to check match for data, then add to zip
    if match is not None:
        zip = match.group(1)
        # if zip has data, then run through text file for matching zipcode
        if zip != "":
            file = open("zipcodes.txt")
            for line in file:
                if zip in line:
                    # retrieve the town and state, starting at the 6th place(iteration) on the line
                    town_state = line[6:]
                    # add town and state to the packet, after being formatted into "proper HTTP"
                    packet = location.format(town_state)
                    break  # get out of the loop
                # if zip has no data, then it's an invalid format
                else:
                    packet = location.format("No Town Found for that Zip")
            file.close()
        # if zip is None then invalid format
    else:
        packet = location.format("Invalid Format")

    # print out packet for testing purposes, encode back to byte, then transmit to excel
    print(packet)

    packet = packet.encode("utf-8")
    conn.sendall(packet)
    # print out the address for nice looking output, even though its pretty much irrelevant
    print("Sent packet back to:", rem_addr, "\n")

    #close out connection
    conn.close()
