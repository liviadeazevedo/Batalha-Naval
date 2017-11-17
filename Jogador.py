from Navio import *
from Tabuleiro import *

class Jogador:
    """Classe referente ao jogadores do jogo.
        *Atributos:
            -tabuleiro ('Tabuleiro'): Estado do tabuleiro durante o jogo;
            -navios (List de 'Navio'): Lista de navios presentes no tabuleiro. 

        OBS: Deixei os métodos deleters por questão de padrão. Podem ser retirados."""
    def __init__(self):
        self.__tabuleiro = Tabuleiro()
        self.__navios = []

    @property
    def tabuleiro(self):
        """ Propriedade ('get') de tabuleiro"""
        return self.__tabuleiro

    @tabuleiro.deleter
    def tabuleiro(self):
        """ 'deleter' de tabuleiro"""
        del self.__tabuleiro

    @property
    def navios(self):
        """ Propriedade ('get') de navios"""
        return self.__navios

    @navios.deleter
    def navios(self):
        """ 'deleter' de tabuleiro"""
        del self.__navios

    def incluirNavio(self,navio):
        """Método que inclui um navio no fim da lista de navios do referido jogador.
            *Parâmetros:
                -navio: Navio a ser inserido na lista.

            *Retorno: booleano -> Operação sucedida ou não."""
        self.__navios.append(navio)
        return True

    def removerNavio(self,idx):
        """Método que remove um determinado navio, dado seu index (idx), na lista de navios do referido jogador.
            *Parâmetros:
                -idx: Índice do navio na lista de navios a ser removido. 
            
            *Retorno: booleano -> Operação sucedida ou não."""
        if idx < 0:
            return False
        else:
            del self.__navios[idx]
            return True

    def limparPreenchimentoPrevio(self,list_aux):
        """Método auxiliar para o método 'posicionarNavio' para controle de inserção de um navio no tabuleiro.
        Caso perceba alguma colisão na inserção do navio nas determinadas posições, este método reseta as posições
        preenchidas anteriormente pelo método.
            *Parâmetros:
                -list_aux: Lista auxiliar que salva as posições preenchidas durante a inserção de um novo navio no tabuleiro."""
        for t in list_aux:
            self.tabuleiro.tabMatriz[t[0],t[1]] = NUM_VAZIO_TABULEIRO


    def posicionarNavio(self,pos,navio):
        """ Método que posiciona o novo navio no tabuleiro do jogador.
            *Parâmetros:
                -pos: Posição de inserção do navio. 
                      Ex: A1-A4 , B5-D5, ... (supondo que a entrada esteja correta. Verificação é feita antes do método ser
                      chamado);
                -navio: Navio a ser inserido.

            *Retorno: booleano -> Operação bem sucedida ou não."""

        numeropos1 = int(pos[1:pos.find('-')])
        numeropos2 = int(pos[pos.find('-')+2:])
        
        diff = numeropos2 - (numeropos1 - 1)

        count = 0
        tabx = Tabuleiro.LETRAS_POSX[pos[0].upper()]
        taby = numeropos1
        list_aux = []

        if pos[0].upper() == pos[pos.find('-')+1].upper() and diff == navio.numCasas: #Posicionar na horizontal
            
            while count < navio.numCasas:
                if self.tabuleiro.tabMatriz[tabx,(taby-1) + count] == NUM_VAZIO_TABULEIRO:
                    self.tabuleiro.tabMatriz[tabx,(taby-1) + count] = NUM_NAVIO_TABULEIRO
                    navio.adicionarPosicao(pos[0].upper() + str(taby + count))
                    list_aux.append((tabx,(taby-1) + count))
                else:
                    self.limparPreenchimentoPrevio(list_aux)
                    navio.limparListaPosicoes()
                    del list_aux
                    return False

                count += 1

            self.incluirNavio(navio)
            return True

        if numeropos1 == numeropos2 and pos[0].upper() != pos[pos.find('-')+1].upper() and diff == 1: #Posicionar na vertical
            
            while count < navio.numCasas:

                if self.tabuleiro.tabMatriz[tabx + count,(taby-1)] == NUM_VAZIO_TABULEIRO:
                    self.tabuleiro.tabMatriz[tabx + count,(taby-1)] = NUM_NAVIO_TABULEIRO
                    navio.adicionarPosicao(LETRAS_TABULEIRO[tabx + count] + str(taby))
                    list_aux.append((tabx,(taby-1) + count))
                else:
                    self.limparPreenchimentoPrevio(list_aux)
                    navio.limparListaPosicoes()
                    del list_aux
                    return False

                count += 1

            self.incluirNavio(navio)
            return True

        return False

    def atacarOponente(self,jogador,pos):
        """ Método que executa a jogada do jogador perante ao oponente.
            *Parâmetros:
                -jogador: Jogador Oponente
                -pos: Posição do ataque. 
                        Ex: "A1", "J9", "E4"

            *Retorno: (boolean,boolean,boolean) -> 1) Operação sucedida ou não; 
                                                    2) Acertou ou não um navio (serve para manter o turno do jogador); 
                                                    3) Navio destruído ou não."""

        posicaoLetra = pos[0].upper()
        posicaoNum = int(pos[1:])
        posicao = pos.upper()

        if (posicaoLetra in LETRAS_TABULEIRO) and (posicaoNum >= 1 and posicaoNum <= TAM_PADRAO) and (not (posicao in jogador.tabuleiro.listaJaAtingidas)):

            tabx = Tabuleiro.LETRAS_POSX[posicaoLetra]
            taby = posicaoNum-1
            count = 0
            
            if jogador.tabuleiro.tabMatriz[tabx,taby] == NUM_VAZIO_TABULEIRO:
                jogador.tabuleiro.tabMatriz[tabx,taby] = NUM_TIRO_TABULEIRO
                jogador.tabuleiro.adicionarPosicaoJaEscolhida(posicao)
                return (True,False,False)

            if jogador.tabuleiro.tabMatriz[tabx,taby] == NUM_NAVIO_TABULEIRO:
                jogador.tabuleiro.tabMatriz[tabx,taby] = NUM_NAVIO_TIRO_TABULEIRO
                jogador.tabuleiro.adicionarPosicaoJaEscolhida(posicao)

                #Remover na lista de posições do navio específico a posição que em que foi atingido.
                while count < len(jogador.navios):
                    if posicao in jogador.navios[count].listaPosicoes:
                        opSuccs,removerNav = jogador.navios[count].removerPosicao(posicao)

                        if opSuccs and removerNav:
                            jogador.removerNavio(count)
                            return (True,True,True)
                        elif opSuccs and (not removerNav):
                            return (True,True,False)
                    
                    count += 1    
            
            return (False,False,False)    
        else:
            return (False,False,False)


        



    
