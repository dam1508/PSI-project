import json


def readConfigFile(file_path):
    with open(file_path) as f:
        content = json.load(f)
        TUNNEL_CLIENT_HOST = content["TUNNEL_CLIENT_HOST"]
        TUNNEL_CLIENT_PORT = content["TUNNEL_CLIENT_PORT"]
        TUNNEL_SERVER_HOST = content["TUNNEL_SERVER_HOST"]
        TUNNEL_SERVER_PORT = content["TUNNEL_SERVER_PORT"]
        HOST_OUT = content["HOST_OUT"]
        PORT_OUT = content["PORT_OUT"]
        BUFSIZE = content["BUFSIZE"]
        XOR_KEY = content["XOR_KEY"]

        return TUNNEL_CLIENT_HOST, TUNNEL_CLIENT_PORT, TUNNEL_SERVER_HOST, TUNNEL_SERVER_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY
