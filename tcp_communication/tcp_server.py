import socket
from encryption.encrypt import decrypt_data

""" This class defines a C-like struct """


def main():
    PORT = 2300
    server_addr = ('localhost', PORT)
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    try:
        # bind the server socket and listen
        ssock.bind(server_addr)
        print("Bind done")
        ssock.listen(16)
        print("Server listening on port {:d}".format(PORT))

        while True:
            csock, client_address = ssock.accept()
            print("Accepted connection from {:s}".format(client_address[0]))
            buff = csock.recv(512)
            while buff:
                print("\nReceived {:d} bytes".format(len(buff)))
                data = decrypt_data(buff.decode(), "key")
                print(data)
                print("Sending it back.. ", end='')
                # nsent = csock.send(payload_in)
                # print("Sent {:d} bytes".format(nsent))
                buff = csock.recv(512)

            print("Closing connection to client")
            print("----------------------------")
            csock.close()

    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    except KeyboardInterrupt:
        ssock.close()
    finally:
        print("Closing socket")
        ssock.close()


if __name__ == "__main__":
    main()
