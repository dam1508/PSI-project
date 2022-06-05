import socket
from readJSON import readConfigFile
from encryption.encrypt import decrypt_data, encrypt_data



def main():
    SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")
    server_addr = (TCP_HOST, TCP_PORT)
    server_address_port = (SENDER_HOST, SENDER_PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)

    socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    socketUDP.bind(server_address_port)

    while True:

        # print("Server listening on port {:d}".format(PORT))
        data_address = socketUDP.recvfrom(BUFSIZE)
        data = data_address[0]
        address = data_address[1]
        sock.sendall(encrypt_data(data.decode(), XOR_KEY).encode())

        data = sock.recv(BUFSIZE)
        print("Received data from TCP")
        # data decryption
        data = decrypt_data(data.decode(), XOR_KEY)
        # print("DATA received after crypting", data)

    # print("MSG", msg)
    # print(decryptOrEncrypt(msg.decode(), XOR_KEY))
        print("Sending data by UDP")
        socketUDP.sendto(data.encode(), address)


if __name__ == "__main__":
    main()
