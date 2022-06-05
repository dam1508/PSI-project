# simple Python socket UDP server
# (C) G.Blinowski for PSI 2021

import socket
import sys

HOST = 'localhost'  # Standard loopback interface address (localhost)
# BUFSIZE = 512
BUFSIZE = 512
if len(sys.argv) < 2:
    print("no port, using 8001")
    port = 8001
else:
    port = int(sys.argv[1])

print("Will listen on ", HOST, ":", port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, port))
    i = 1
    while True:
        data_address = s.recvfrom(BUFSIZE)
        data = data_address[0]
        address = data_address[1]
        print("Message from Client:{}".format(data))
        print("Client IP Address:{}".format(address))

        if not data:
            print("Error in datagram?")
            break
        # echo back data - NOTE - compare send() and sendall()!
        s.sendto(data, address)
        print('sending dgram #', i)
        i += 1
