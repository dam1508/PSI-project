import socket
import sys
import random
from ctypes import *

class Payload(Structure):
    _fields_ = [("id", c_uint32),
                ("counter", c_uint32),
                ("temp", c_float)]


def main():
    server_addr = ('localhost', 2300)
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)

    try:
        s.connect(server_addr)
        print("Connected to {:s}".format(repr(server_addr)))

        for i in range(1):
            print("")
            payload_out = Payload(1, i, random.uniform(-10, 30))
            print("Sending id={:d}, counter={:d}, temp={:f}".format(payload_out.id,
                                                                    payload_out.counter,
                                                                    payload_out.temp))
            payload_out = "abcdaaaaaaaaaaaaaaaa".encode()
            nsent = s.sendall(payload_out)
    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    finally:
        print("Closing socket")
        s.close()


if __name__ == "__main__":
    main()
