#!/usr/bin/env python3

""" server.py - Echo server for sending/receiving C-like structs via socket
References:
- Ctypes: https://docs.python.org/3/library/ctypes.html
- Sockets: https://docs.python.org/3/library/socket.html
"""

import socket
import sys
import random
from ctypes import *


""" This class defines a C-like struct """
class Payload(Structure):
    _fields_ = [("id", c_uint32),
                ("counter", c_uint32),
                ("temp", c_float)]


def main():
    serverAddress = "127.0.0.1"
    serverPort = 20001
    bufferSize = 1024
    serverMessage = "Connected to UDP Server, Welcome!"
    bytesToSend = str.encode(serverMessage)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serverSocket:
        serverSocket.bind((serverAddress, serverPort))

        print("UDP Server up and listening")

        while (True):
            dataAddress = serverSocket.recvfrom(bufferSize)
            message = dataAddress[0]
            address = dataAddress[1]

            clientMessage = "Message :{}".format(message)
            clientIP = "Client IP:{}".format(address)

            # print(clientMessage)
            print("Received message")

            serverSocket.sendto(bytesToSend, address)


if __name__ == "__main__":
    main()