import socket            
import security
from colorama import Fore, Style, Back

s = socket.socket()   
host = input(Fore.CYAN+"Enter hostname: ")
port = 1234

try:
    key = input("Enter key: ")

    s.connect((host, port))

    print(Fore.GREEN+"Connected to ", host)

    print('\n\n')

    while 1:
        incoming_message = s.recv(1024)
        incoming_message = security.decrypt(key, bytes(incoming_message))
        if incoming_message.decode() == "quit":
            break
        print(Fore.LIGHTWHITE_EX+"Spy-1 >>",incoming_message.decode())
        raw_message = input(str(Fore.LIGHTYELLOW_EX+"Spy-2 >> "))
        encrypted_message = security.encrypt(key, bytes(raw_message.encode()))
        s.send(encrypted_message)
        if raw_message == "quit":
            print(Fore.RED+"Connection closed")
            break 
except:
    print(Fore.RED+"Connection failed")
    s.close()