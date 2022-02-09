import sys
from cryptography.fernet import Fernet

def  encrypt(key, message): #Will encrypt the message
    f = Fernet(key)
    encrypted = f.encrypt(message)
    return encrypted

def decrypt(key, message): #Will decrypt the message
    f = Fernet(key)
    decrypted = f.decrypt(message)
    return decrypted


