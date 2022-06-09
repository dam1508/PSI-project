import socket
from readJSON import readConfigFile
from encryption.encrypt import decrypt_data, encrypt_data


def main():
    SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")
    tunnel_client_address = (TCP_HOST, TCP_PORT)
    sender_address = (SENDER_HOST, SENDER_PORT)
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.connect(tunnel_client_address)

    socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    socketUDP.bind(sender_address)
    print("Listening...")
    while True:
        try:
            # print("Server listening on port {:d}".format(PORT))
            data_address = socketUDP.recvfrom(BUFSIZE)
            data = data_address[0]
            address = data_address[1]
            # data, address = socketUDP.recvfrom(BUFSIZE)
            socketTCP.sendall(encrypt_data(data.decode(), XOR_KEY).encode())
            print("Sent data to TCP")
            data = socketTCP.recv(BUFSIZE)
            print("Received data from TCP")
            # data decryption
            data = decrypt_data(data.decode(), XOR_KEY)
            # print("DATA received after crypting", data)

            # print("MSG", msg)
            # print(decryptOrEncrypt(msg.decode(), XOR_KEY))
            print("Sending data by UDP")
            socketUDP.sendto(data.encode(), address)
        except KeyboardInterrupt:
            print()
            print("Program exiting")
            quit()


if __name__ == "__main__":
    main()
