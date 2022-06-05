import json


def readConfigFile(file_path):
    with open(file_path) as f:
        content = json.load(f)
        SENDER_HOST = content["SENDER_HOST"]
        SENDER_PORT = content["SENDER_PORT"]
        TCP_HOST = content["TCP_HOST"]
        TCP_PORT = content["TCP_PORT"]
        HOST_OUT = content["HOST_OUT"]
        PORT_OUT = content["PORT_OUT"]
        BUFSIZE = content["BUFSIZE"]
        XOR_KEY = content["XOR_KEY"]

        return SENDER_HOST, SENDER_PORT, TCP_HOST, TCP_PORT, HOST_OUT, PORT_OUT, BUFSIZE, XOR_KEY
