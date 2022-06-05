import json
import socket
import sys
import select
import errno


HOSTipv4 = '25.31.71.151'
BUFSIZE = 512


def Work(): 
  return True

def readConfigFile(file_path):
  
  with open(file_path) as f:
    content = json.load(f)
    print(content)
    HOST = content["HOST"]
    PORT = content["PORT"]
    HOST_OUT = content["HOST_OUT"]
    PORT_OUT = content["PORT_OUT"]
    XOR_KEY = content["XOR_KEY"]

    return HOST, PORT, HOST_OUT, PORT_OUT, XOR_KEY


HOST, PORT, HOST_OUT, PORT_OUT, XOR_KEY = readConfigFile("config.json")


print("Will listen on ", HOST, ":", PORT)

# tcp socket for ipv6
socket_tcp_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
socket_tcp_ipv6.bind((HOST, PORT))
socket_tcp_ipv6.listen( 5 )

# tcp socket for ipv4
socket_tcp_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp_ipv4.bind((HOSTipv4, PORT))
socket_tcp_ipv4.listen( 5 )

# udp socket
socket_udp =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket_udp.setblocking(False)

def decryptOrEncrypt(s, xor_key):
  # function for xor decrypting
 
  for i in range(len(s)):
    s = (s[:i] + chr(ord(s[i]) ^ ord(xor_key)) + s[i + 1:])
     
  return s


while Work():
  socks = [socket_tcp_ipv6, socket_tcp_ipv4]
  ready_socks,_,_ = select.select(socks, [], []) 
  print(ready_socks)
  for sock in ready_socks:
    conn, addr = sock.accept()
    
    with conn:
      print('Connect from: ', addr)
      while True:
        data = conn.recv( BUFSIZE )
        if not data:
          break
        
        # data decryption
        data = decryptOrEncrypt(data.decode(), XOR_KEY)
        # print("DATA received after crypting", data)

        # sending udp
        socket_udp.sendto(data.encode(), (HOST_OUT, PORT_OUT))

        try:
          msg = socket_udp.recv(1024)
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
        conn.sendall(decryptOrEncrypt(msg.decode(), XOR_KEY).encode())

  print("Connection closed by client" )