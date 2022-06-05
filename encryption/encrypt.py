from xorencryption import XOREncryption


def encrypt_data(data: str, key: str) -> str:
    enc = XOREncryption()
    enc.set_key(key=key)
    enc.set_plaintext(plaintext=data)

    return enc.encrypt()


def decrypt_data(data: str, key: str) -> str:
    enc = XOREncryption()
    enc.set_key(key=key)
    enc.set_ciphertext(ciphertext=data)
    return enc.decrypt()
