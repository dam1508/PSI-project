import socket
import sys
import random
from ctypes import *

class Payload(Structure):
    _fields_ = [("id", c_uint32),
                ("counter", c_uint32),
                ("temp", c_float)]






def main():
    msgFromClient = 'a'
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("localhost", 7999)

    bufferSize = 512

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    print(f"Sending {msgFromClient}")
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)

if __name__ == "__main__":
    main()
