from socket import *	# Imports socket module

class TCPconnetion:
    def __init__(self):
        self.host="127.0.0.1"
        self.port=4446
        self.serverConnectionSocket = socket(AF_INET, SOCK_STREAM)
        self.serverConnectionSocket.bind((self.host,self.port))
        
        self.idP1 = 0
        self.idP2 = 1
        self.encoding = 'utf-8'
       
        # guarda os sockets dos clientes
        self.socketsClientes = []
        # guarda os enderecos dos clientes
        self.enderecosClientes = [] # tupla (host, port) dos clientes

        self.serverConnectionSocket.listen(1)
        print("Esperando Jogador 1...")

        self.__registrarConexao()
        
        self.enviarP1("Esperando Jogador 2...")
        print("Esperando Jogador 2...")
        
        self.__registrarConexao()

        # indica para os jogadores quem é o seu adversário (localHost:porta)
        self.enviarP1("Conectado ao Jogador 2 (addr: "+ self.enderecosClientes[self.idP2][0] + ":" + str(self.enderecosClientes[self.idP2][1])  +") \n\n Esperando Espectador (por 20s)...\n")
        
        self.enviarP2("Conectado ao Jogador 1 (addr: " + self.enderecosClientes[self.idP1][0] + ":" + str(self.enderecosClientes[self.idP1][1])  +") \n\n Esperando Espectador (por 20s)...\n")

        # passa a esperar conexão só por 20s
        self.serverConnectionSocket.settimeout(20)
        print("Esperando Espectador (por 20s)...\n")
        
        self.__registrarConexao()
        self.serverConnectionSocket.setblocking(False)

    def __registrarConexao(self):
        try:
            cSocket, cAddr = self.serverConnectionSocket.accept()

            self.socketsClientes.append(cSocket)
            self.enderecosClientes.append(cAddr)
            if len(self.socketsClientes) > 2: #MEXI AQUI
                self.__enviarMensagem("Conectado como Espectador...\n", cSocket)
        except OSError:
            if len(self.socketsClientes) >= 2: 
                print("Sem mais observadores por enquanto.\n")   
        
    def enviarP1(self, msg):
        self.__enviarMensagem(msg, self.socketsClientes[self.idP1])
        
    def enviarP2(self, msg):
        self.__enviarMensagem(msg, self.socketsClientes[self.idP2])
        
    def enviarTodos(self, msg, ignorar=()):
        for socket in self.socketsClientes:
            if self.socketsClientes.index(socket) in ignorar:
                continue
            self.__enviarMensagem(msg, socket)
    
    def __enviarMensagem(self, msg, socket):
        socket.send(bytes(msg, self.encoding))
    
    def receberDeP1(self):
        self.enviarP1("input")
        return self.__receberMensagem(self.socketsClientes[self.idP1])
        
    def receberDeP2(self):
        self.enviarP2("input")
        return self.__receberMensagem(self.socketsClientes[self.idP2])
    
    def __receberMensagem(self, socket):
        data = socket.recv(1024)
        return "".join(map(chr, data))
    
    def fecharConexao(self):
        self.enviarTodos("out")
        self.serverConnectionSocket.close()
