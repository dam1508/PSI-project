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
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)

    try:
        #s.connect(server_addr)
        #print("Connected to {:s}".format(repr(server_addr)))
        print("")
        payload_out = "abcdaaaaaaaaaaaaaaaa".encode()
        s.sendto(payload_out, server_addr)

    except AttributeError as ae:
        print("Error creating the socket: {}".format(ae))
    except socket.error as se:
        print("Exception on socket: {}".format(se))
    finally:
        print("Closing socket")
        s.close()


if __name__ == "__main__":
    main()
