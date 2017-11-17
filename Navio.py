#==================================================CONSTANTES PADRÕES PARA O JOGO==================================================

#OBS: Criei diversas destas constantes para tentar deixar o código o mais flexível possível na hora de alterações pontuais como estas
#dos navios, até para possíveis adições possíveis de novos navios e alterações nas características de cada navio.

#Constantes para a quantidade de casas usadas por tipo de navio.
CASAS_PORTA_AVIAO = 5
CASAS_NAVIO_TANQUE = 4
CASAS_CONTRA_TORPEDOS = 3
CASAS_SUBMARINO = 2

#Constantes para a quantidade de navios usados por tipo de navio.
QTD_PORTA_AVIAO = 1
QTD_NAVIO_TANQUE = 2
QTD_CONTRA_TORPEDOS = 3
QTD_SUBMARINO = 4

#Total de navios usados no jogo.
TOTAL_NAVIOS_JOGO = 10

#Quantidade de tipos de navios no jogo.
QTD_TIPOS_NAVIOS = 4

#Constantes para a abreviação de cada navio. Usado na hora de receber o input do usuário na seleção do navio.
CHAVE_PORTA_AVIAO = "PA"
CHAVE_NAVIO_TANQUE = "NT"
CHAVE_CONTRA_TORPEDOS = "CT"
CHAVE_SUBMARINO = "SUB"

#Constantes para o nome de cada navio usado. Usado na hora de impressão na lógica do jogo.
NOME_PORTA_AVIAO = "Porta Aviao"
NOME_NAVIO_TANQUE = "Navio Tanque"
NOME_CONTRA_TORPEDOS = "Contra Torpedos"
NOME_SUBMARINO = "Submarino"

#Estruturas auxiliares para uso dos métodos para o funcionamento do jogo.
LISTA_CHAVES = [CHAVE_PORTA_AVIAO,CHAVE_NAVIO_TANQUE,CHAVE_CONTRA_TORPEDOS,CHAVE_SUBMARINO]
LISTA_NOMES = [NOME_PORTA_AVIAO,NOME_NAVIO_TANQUE,NOME_CONTRA_TORPEDOS,NOME_SUBMARINO]

#================================================================================================================================

#Informações sobre as peças do Jogo(Navios)
class Navio:
    """Classe que representa um navio presente no jogo.
        *Construtor:
            -num: Número de casas do navio.    
    
        *Atributos:
            -numCasas: Número de casas ocupadas pelo navio;
            -listaPosicoes: Lista que contém as posições que o navio ocupa no tabuleiro. Cada elemento é uma posição, em string,
            possível no tabuleiro. Ex: A1, C3, G4, (...)

        *Atributos Estáticos:
            -NAVIOS_DISPONÍVEIS: Dicionário dos navios disponíveis para o jogo que tem a relação -> (chave_navio: (qtd,nome,casas)).
    OBS: Deixei os métodos deleters por questão de padrão. Podem ser retirados"""


    NAVIOS_DISPONIVEIS = {CHAVE_PORTA_AVIAO: (QTD_PORTA_AVIAO,NOME_PORTA_AVIAO,CASAS_PORTA_AVIAO),
                          CHAVE_NAVIO_TANQUE: (QTD_NAVIO_TANQUE,NOME_NAVIO_TANQUE,CASAS_NAVIO_TANQUE),
                          CHAVE_CONTRA_TORPEDOS: (QTD_CONTRA_TORPEDOS,NOME_CONTRA_TORPEDOS,CASAS_CONTRA_TORPEDOS),
                          CHAVE_SUBMARINO: (QTD_SUBMARINO,NOME_SUBMARINO,CASAS_SUBMARINO)}

    def __init__(self,num):
        self.__numCasas = num
        self.__listaPosicoes = set([])
    
    @property
    def numCasas(self):
        """Propriedade ('get') de numCasas"""
        return self.__numCasas

    @numCasas.deleter
    def numCasas(self):
        """ 'deleter' de numCasas"""
        del self.__numCasas

    @property
    def listaPosicoes(self):
        """Propriedade ('get') de listaPosicoes"""
        return self.__listaPosicoes

    @listaPosicoes.deleter
    def listaPosicoes(self):
        """ 'deleter' de listaPosicoes"""
        del self.__listaPosicoes

    def adicionarPosicao(self,pos):
        """Método que adiciona a posição na lista de posições ocupadas pelo navio.
            *Parâmtros:
                -pos: String que representa um das posições ocupadas pelo navio no tabuleiro.

            *Retorno: boolean -> Operação sucedida ou não."""
        if pos in self.__listaPosicoes:
            return False
        else:
            self.__listaPosicoes.add(pos)
            return True

    def removerPosicao(self,pos):
        """Método que remove uma posição do navio em sua lista.
            *Parâmetros:
                -pos: String da posição no tabuleiro: A1, B4, ... 

            Retorno: (boolean,boolean) -> 1) Operação sucedida ou não; 
                                            2)Remover navio destruído ou não."""
        if not (pos in self.__listaPosicoes):
            return (False,False)
        else:
            self.__listaPosicoes.remove(pos)

            if len(self.__listaPosicoes) == 0:
                return (True,True)
            else:
                return (True,False)

    def limparListaPosicoes(self):
        """Método que reseta a lista de posições do navio."""
        self.__listaPosicoes.clear()

class PortaAviao(Navio):
	"""Classe filha de 'Navio' que representa o Porta Avião."""
    def __init__(self):
        super(PortaAviao, self).__init__(CASAS_PORTA_AVIAO)

class NavioTanque(Navio):
    """Classe filha de 'Navio' que representa o Navio Tanque."""
    def __init__(self):
        super(NavioTanque, self).__init__(CASAS_NAVIO_TANQUE)

class ContraTorpedos(Navio):
    """Classe filha de 'Navio' que representa o Contra Torpedo."""
    def __init__(self):
        super(ContraTorpedos, self).__init__(CASAS_CONTRA_TORPEDOS)

class Submarino(Navio):
    """Classe filha de 'Navio' que representa o Submarino."""
    def __init__(self):
        super(Submarino, self).__init__(CASAS_SUBMARINO)

class NavioFactory(object):
    """Classe que aplica o padrão de projeto 'Abstract Factory', para a criação dos navios no Jogo."""

    #def __init__(self):
    #    super(NavioFactory, self).__init__()

    @staticmethod
    def criarNavio(chaveNavio):
        """Factory Method para a construção dos navios.
            *Parâmetros:
                -chaveNavio: Abreviação que representa o navio."""
        if chaveNavio == CHAVE_PORTA_AVIAO:
            return PortaAviao()
        elif chaveNavio == CHAVE_NAVIO_TANQUE:
            return NavioTanque()
        elif chaveNavio == CHAVE_CONTRA_TORPEDOS:
            return ContraTorpedos()
        elif chaveNavio == CHAVE_SUBMARINO:
            return Submarino()
        