from pbkdf2 import PBKDF2
from hashlib import sha256
import hashlib, os, binascii, secrets, pyaes

#masterpw = "master"
#masterpw_hash = hashlib.sha256(masterpw.encode()).hexdigest()

"""
def confirm_pw(masterpw):
    # Will get hash from sql or file
    if(masterpw == masterpw_hash):
        return True
    return False
"""

def make_salt():
    f = open('keyfile.txt', 'w')
    salt = os.urandom(16)
    f.write(binascii.hexlify(salt).decode('utf-8'))

def get_salt():
    print("Getting Salt")
    f = open('keyfile.txt', 'r')
    salt = f.read()
    return salt

def make_masterkey(masterpw, salt):
    print("Making MasterKey")
    key = PBKDF2(masterpw, salt, iterations=100000).read(32)
    return key

def encrypt(plaintext, key):
    print("Encrypting")
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    cipher = aes.encrypt(plaintext)
    return cipher, iv

def decrypt(ciphertext, iv, key):
    print("Decrpyting")
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    return decrypted

# make_salt()
# salt = get_salt()
# key = make_masterkey("masterpw", salt)[0]

# Master Key Salt must be saved on first config
# Then when the user comes back, we take the master pw they enter
# salt with the saved salt, and use as our master key

# cipher = encrypt("password", key)

# plain = decrypt(cipher[0], cipher[1], key)

# print("Salt : ", salt)
# print("Key : ", key)
# print("Ciphertext : ", cipher)
# print("Plaintext : ", plain)
