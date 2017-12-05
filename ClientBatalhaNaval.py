# PLAYER 2
print(" PLAYER 1 ")

host="127.0.0.1"            # Set the server address to variable host

port=4446               # Sets the variable port to 4444

from socket import *             # Imports socket module

s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
msg = " "
s.connect((host,port))          # Connect to server address


while(True):
    data=s.recv(1024)
    msg = "".join(map(chr, data))
    if(msg.endswith("input")):
        if len(msg) > len("input"):
            msg = msg.rsplit("input", maxsplit=1)[0]
            print(msg)
        msgEnvio = input()
        if len(msgEnvio.rsplit()) == 0:
            msgEnvio = "vazio"
        s.send(bytes(msgEnvio, 'utf-8'))
    else:
        if msg.endswith("out") :
            if len("out") != len(msg):
                nsg = msg.rsplit("out", maxsplit=1)[0]
                print(msg)
            break
        print(msg)
    
print("out")
s.close()