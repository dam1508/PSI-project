import json
import socket
import sys
import select
import errno
from readJSON import readConfigFile
from encryption.encrypt import decrypt_data, encrypt_data


def Work():
    return True


SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY = readConfigFile("config.json")

print("Will listen on ", TCP_HOST, ":", TCP_PORT)

# tcp socket for ipv6
socket_tcp_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
socket_tcp_ipv6.bind((TCP_HOST, TCP_PORT))
socket_tcp_ipv6.listen(5)

# tcp socket for ipv4
socket_tcp_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp_ipv4.bind((TCP_HOST, TCP_PORT))
socket_tcp_ipv4.listen(5)

# udp socket
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket_udp.setblocking(False)


while Work():
    socks = [socket_tcp_ipv6, socket_tcp_ipv4]
    ready_socks, _, _ = select.select(socks, [], [])
    print(ready_socks)
    for sock in ready_socks:
        conn, addr = sock.accept()

        with conn:
            print('Connect from: ', addr)
            while True:
                data = conn.recv(BUFSIZE)
                if not data:
                    break

                # data decryption
                data = decrypt_data(data.decode(), XOR_KEY)
                # print("DATA received after crypting", data)

                # sending udp
                socket_udp.sendto(data.encode(), (HOST_OUT, PORT_OUT))

                try:
                    msg = socket_udp.recv(512)
                    # print("MSG", msg)

                # checking for errors
                except socket.error as e:
                    err = e.args[0]

                    if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                        print('No data available')
                        continue

                    else:
                        # a "real" error occurred
                        print(e)

                # print("MSG", msg)
                # print(decryptOrEncrypt(msg.decode(), XOR_KEY))
                print("Sending data by tcp")
                conn.sendall(encrypt_data(msg.decode(), XOR_KEY).encode())

    print("Connection closed by client")
