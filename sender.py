import socket
import sys
from readJSON import readConfigFile


def main():
    SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")
    msgFromClient = sys.argv[1]
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = (SENDER_HOST, SENDER_PORT)

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    print(f"Sending: {msgFromClient}")
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(BUFSIZE)

    msg = "Message from Server: {}".format(msgFromServer[0].decode())

    print(msg)


if __name__ == "__main__":
    main()
