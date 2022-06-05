import socket
from encryption.encrypt import encrypt_data

DATA = "abccabccabccabccabccc"


def receive_data():
    PORT = 2300
    server_addr = ('localhost', PORT)
    ssock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ssock.bind(server_addr)
        #print("Server listening on port {:d}".format(PORT))
        buff = ssock.recv(512)

        return buff.decode()

    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    except KeyboardInterrupt:
        ssock.close()


def main():
    data = receive_data()
    server_addr = ('localhost', 2400)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(server_addr)
        print("Connected to {:s}".format(repr(server_addr)))

        data = encrypt_data(data, "key")

        s.send(data.encode())

    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    finally:
        print("Closing socket")
        s.close()


if __name__ == "__main__":
    main()
