import numpy as np
import string as s

#==================================================CONSTANTES PADRÕES PARA O JOGO==================================================

#Tamanho nxn do tabuleiro.
TAM_PADRAO = 10

#Letras disponíveis dado o tamanho.
LETRAS_TABULEIRO = s.ascii_uppercase[0:TAM_PADRAO]

#Index's para representar os diferentes estados do tabuleiro durante o jogo.
NUM_VAZIO_TABULEIRO = 0
NUM_TIRO_TABULEIRO = 1
NUM_NAVIO_TABULEIRO = 2
NUM_NAVIO_TIRO_TABULEIRO = 3

#================================================================================================================================

def criarDictLetrasNum():
	"""Método que cria um dicionário tal que: (letra:posição na string string.ascii_uppercase)."""
	LETRAS_POSX = {}
	
	for i in range(0,TAM_PADRAO):
		LETRAS_POSX[LETRAS_TABULEIRO[i]] = i

	return LETRAS_POSX

class Tabuleiro:
	"""Classe que representa as características do tabuleiro do jogo Batalha Naval.
		*Construtor:
			

	OBS: Deixei os métodos deleters por questão de padrão. Podem ser retirados"""

	LETRAS_POSX = criarDictLetrasNum()

	def __init__(self):
		self.__tabMatriz = np.zeros([TAM_PADRAO,TAM_PADRAO]).astype(int) #0 -> vazio; 1 -> atingido; 2 -> ocupada por algum navio
		self.__listaJaAtingidas = [] #Acelerar o processo de verificação das casas já atingidas(além do histórico dos tiros)
		#Método sort para ordenar em ordem alfabética as posições.

	#OBS: Deixei os métodos deleters por questão de padrão. Podem ser retirados.

	@property
	def tabMatriz(self):
		"""Propriedade de tabMatriz"""
		return self.__tabMatriz

	@tabMatriz.deleter
	def tabMatriz(self):
		del self.__tabMatriz

	@property
	def listaJaAtingidas(self):
		"""Propriedade de listaJaAtingidas"""
		return self.__listaJaAtingidas

	@listaJaAtingidas.deleter
	def listaJaAtingidas(self):
		del self.__listaJaAtingidas

	def imprimirSeuTabuleiro(self):
		posx = 0
		posy = 0
		c = 0
		count_letter = 0
		print("\t",end="")

		for i in range(0,TAM_PADRAO):
			print(i+1,end=" ")

		print()

		print("\t",end="")

		for i in range(0,TAM_PADRAO):
			print("-",end=" ")

		for i in range(0,TAM_PADRAO**2):
			if c % TAM_PADRAO == 0:
				print()
				print("    ",LETRAS_TABULEIRO[count_letter],"|",end="")
				count_letter += 1

				if c != 0:
					posx += 1

				posy = 0

			#print(0, end=" ")
			print(self.__tabMatriz[posx,posy], end=" ")
			c += 1
			posy += 1

		#print()
		print("\n")
		print("Legenda:","\n","0 -> Disponível","\n","1 -> Atingido","\n", "2 -> Posição dos navios","\n","3 -> Navio atingido")

	def adicionarPosicaoJaEscolhida(self,pos):
		self.__listaJaAtingidas.append(pos.upper())
		self.__listaJaAtingidas.sort()

		