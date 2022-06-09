import socket
from readJSON import readConfigFile


def main():
    SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")

    print("Will listen on ", HOST_OUT, ":", PORT_OUT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST_OUT, PORT_OUT))
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


if __name__ == "__main__":
    main()
