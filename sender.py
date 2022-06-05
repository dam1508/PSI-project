import socket
import sys
import random
from ctypes import *
from readJSON import readConfigFile

class Payload(Structure):
    _fields_ = [("id", c_uint32),
                ("counter", c_uint32),
                ("temp", c_float)]



def main():
    SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")
    msgFromClient = 'a'
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = (SENDER_HOST, SENDER_PORT)


    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    print(f"Sending {msgFromClient}")
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("xd")
    msgFromServer = UDPClientSocket.recvfrom(BUFSIZE)

    msg = "Message from Server {}".format(msgFromServer[0].decode())

    print(msg)

if __name__ == "__main__":
    main()
