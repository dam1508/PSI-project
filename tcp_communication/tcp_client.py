import socket
from readJSON import readConfigFile
from encryption.encrypt import decrypt_data, encrypt_data

BUFSIZE = 512


def receive_data():
    PORT = 7999
    server_addr = ('localhost', PORT)
    ssock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ssock.bind(server_addr)
        # print("Server listening on port {:d}".format(PORT))
        buff = ssock.recv(512)
        print(f"Received data from UDP")
        return buff.decode()

    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    except KeyboardInterrupt:
        ssock.close()


def main():
    HOST, PORT, HOST_OUT, PORT_OUT, XOR_KEY = readConfigFile("config.json")
    server_addr = ('localhost', PORT)
    serverAddressPort = ('localhost', 7999)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    sock.connect(server_addr)

    while True:
        data = receive_data()

        print("Sending data by TCP")
        sock.sendall(encrypt_data(data, XOR_KEY).encode())

        data = sock.recv(BUFSIZE)
        print("Received data from TCP")
        # data decryption
        data = decrypt_data(data.decode(), XOR_KEY)
        # print("DATA received after crypting", data)

    # print("MSG", msg)
    # print(decryptOrEncrypt(msg.decode(), XOR_KEY))
        print("Sending data by UDP")
        socketUDP.sendto(data.encode(), serverAddressPort)


if __name__ == "__main__":
    main()
