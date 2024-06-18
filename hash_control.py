from pbkdf2 import PBKDF2
from hashlib import sha256
import os, binascii, secrets, pyaes

def make_salt():
    print("\nMaking Salt")
    f = open('keyfile.txt', 'w')
    salt = os.urandom(16)
    f.write(binascii.hexlify(salt).decode('utf-8'))

def get_salt():
    print("\nGetting Salt")
    f = open('keyfile.txt', 'r')
    salt = f.read()
    return binascii.unhexlify(salt)

def make_masterkey(masterpw, salt):
    print("\nMaking MasterKey")
    key = PBKDF2(masterpw, salt, iterations=100000).read(32)
    return key

def encrypt(plaintext, key):
    print("\nEncrypting")
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    cipher = aes.encrypt(plaintext)
    return cipher, iv

def decrypt(ciphertext, iv, key):
    print("\nDecrpyting")
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    return decrypted

