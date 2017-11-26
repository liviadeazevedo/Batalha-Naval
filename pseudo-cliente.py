# PLAYER 1
print(" PLAYER 1 ")

host="127.0.0.1"            # Set the server address to variable host

port=4446               # Sets the variable port to 4444

from socket import *             # Imports socket module

s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
msg = " "
s.connect((host,port))          # Connect to server address

while(msg != "out"):
    if msg.strip() != "input":
        data=s.recv(1024)
        msg = "".join(map(chr, data))
    if(msg.strip() == "input"):
        msgEnvio = input()
        s.send(bytes(msgEnvio, 'utf-8'))
        msg = ""
    else:
        print(msg)
print("out")
s.close()