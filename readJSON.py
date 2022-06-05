import json


def readConfigFile(file_path):
    with open(file_path) as f:
        content = json.load(f)
        print(content)
        HOST = content["TCP_HOST"]
        PORT = content["TCP_PORT"]
        HOST_OUT = content["HOST_OUT"]
        PORT_OUT = content["PORT_OUT"]
        XOR_KEY = content["XOR_KEY"]

        return HOST, PORT, HOST_OUT, PORT_OUT, XOR_KEY
