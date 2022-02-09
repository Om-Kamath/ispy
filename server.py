import socket        
from cryptography.fernet import Fernet
import security    
from colorama import Fore, Style, Back

 
try:
    s = socket.socket()        
    host = socket.gethostname()

    print(Fore.CYAN+"Hostname: ", host)
    port = 1234

    s.bind((host, port))
    print("Socket bound to port: ", port)
    s.listen(5)

    key = Fernet.generate_key()

    print(Fore.MAGENTA+"The key is:" , key.decode())
    print(Fore.LIGHTRED_EX+"KINDLY DO NOT SHARE THE KEY WITH ANYONE ELSE")

    print(Fore.GREEN+"Socket is listening")

    conn, addr = s.accept()

    print(Fore.GREEN+"Connected")

    print('\n\n')

    while 1:
        raw_message = input(str(Fore.LIGHTYELLOW_EX+"Spy-1 >> "))
        encrypted_message = security.encrypt(key, bytes(raw_message.encode()))
        conn.send(encrypted_message)
        if raw_message == "quit":
            print(Fore.RED+"Connection closed")
            break 
        incoming_message = conn.recv(1024)
        incoming_message = security.decrypt(key, bytes(incoming_message))
        if incoming_message.decode() == "quit":
            print(Fore.RED+"Connection closed")
            break
        print(Fore.LIGHTWHITE_EX+"Spy-2 >>", incoming_message.decode())
except:
    print(Fore.RED+"Connection failed")
    s.close()