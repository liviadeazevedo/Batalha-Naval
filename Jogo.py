from random import randint
from Jogador import *

MSG_JOG1 = "Jog1"
MSG_JOG2 = "Jog2"

class Jogo:
	"""Informações sobre o jogo.
	OBS: Deixei os métodos deleters por questão de padrão. Podem ser retirados."""
	def __init__(self):

		self.__j1 = Jogador()
		self.__j2 = Jogador()

	@property
	def j1(self):
		"""Propriedade de j1"""
		return self.__j1

	@j1.deleter
	def j1(self):
		del self.__j1

	@property
	def j2(self):
		"""Propriedade de j2"""
		return self.__j2

	@j2.deleter
	def j2(self):
		del self.__j2

	def selecaoJogadorMaquinaTiro(self):
		LETRAS_TABULEIRO = s.ascii_uppercase[0:TAM_PADRAO]

		letra = LETRAS_TABULEIRO[randint(0,TAM_PADRAO-1)]
		numero = str(randint(0,TAM_PADRAO-1))

		tiro = letra + numero

		return tiro

	def imprimirListaNavios(self,dict_aux):
    
		print("Navios Disponíveis:\n")

		for i in LISTA_CHAVES:
			print(i + ")",Navio.NAVIOS_DISPONIVEIS[i][1] + "-->","Casas Ocupadas:",str(Navio.NAVIOS_DISPONIVEIS[i][2]) + ";","Quantidade:",dict_aux[i])

		print()

	def criarDictNavioValor(self):

		dict_aux = {}

		for c,v in Navio.NAVIOS_DISPONIVEIS.items(): 
			dict_aux[c] = v[0]

		return dict_aux

	def resetarDictNavioValor(self, dict_aux):

		for c,v in Navio.NAVIOS_DISPONIVEIS.items(): 
			dict_aux[c] = v[0]


	def selecionarNavio(self,chaveNavio,dict_aux): #Cada jogador deve chamar esse método a cada navio 

		if not chaveNavio in Navio.NAVIOS_DISPONIVEIS.keys() or dict_aux[chaveNavio] == 0:
			return (None,False)

		novo_navio = NavioFactory.criarNavio(chaveNavio)

		return (novo_navio,True)

	def escolherNavio(self,j1Vez):
		jFluxo = True
		validezInput = False
		validezInputPos = False
		resultEsperado = False

		qtd_total_navios = TOTAL_NAVIOS_JOGO
	
		dict_aux = self.criarDictNavioValor()

		while jFluxo:

			self.imprimirListaNavios(dict_aux)

			while not validezInput:
				print("----------------------------------------------------------------------------------------------------")
				abrevNavio = input("Digite a abreviação do navio que queria posicionar no tabuleiro:\n----------------------------------------------------------------------------------------------------\n").upper()
				navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)

				if not validezInput:
					print("ENTRADA INCORRETA OU NAVIO ESGOTADO. POR FAVOR, TENTE NOVAMENTE\n")
				
			while not resultEsperado:
				print("----------------------------------------------------------------------------------------------------")
				posNavio = input("Digite a posição que deseja colocar seu " + Navio.NAVIOS_DISPONIVEIS[abrevNavio][1] + "(Casas: " + str(navioSel.numCasas) + ")" + ".\nOBS: Considere a ordem das posições da esq para dir(horizontal) e de cima para baixo(vertical)\nEXEMPLOS: A1-A5, B1-E1, F3-F5" +":\n----------------------------------------------------------------------------------------------------\n").upper()
				validezInputPos = self.verificarValidezInputPosicaoNavio(posNavio)

				if not validezInputPos:
					print("ENTRADA INCORRETA. POR FAVOR, TENTE NOVAMENTE\n")
					#print("TABULEIRO ATUAL:\n")
					#if j1Vez:
					#	self.j1.tabuleiro.imprimirSeuTabuleiro()
					#else:
					#	self.j2.tabuleiro.imprimirSeuTabuleiro()

					continue

				if j1Vez:
					resultEsperado = self.j1.posicionarNavio(posNavio,navioSel)
				else:
					resultEsperado = self.j2.posicionarNavio(posNavio,navioSel)

				if not resultEsperado:
					print("POSICAO JA OCUPADA, QUANTIDADE DE POSICOES INCORRETAS DADO O NAVIO OU COLISAO DE POSICAO. POR FAVOR, SELECIONE OUTRA.\n")
					#print("TABULEIRO ATUAL:\n")
					#if j1Vez:
					#	self.j1.tabuleiro.imprimirSeuTabuleiro()
					#else:
					#	self.j2.tabuleiro.imprimirSeuTabuleiro()


			dict_aux[abrevNavio] -= 1
			qtd_total_navios -= 1
			validezInput = False
			validezInputPos = False
			resultEsperado = False

			print("====================================================")
			print("NAVIO POSTO COM SUCESSO. SELECIONE O PRÓXIMO.\n\n","TABULEIRO ATUAL:\n")

			if j1Vez:
				self.j1.tabuleiro.imprimirSeuTabuleiro()
			else:
				self.j2.tabuleiro.imprimirSeuTabuleiro()

			print("====================================================")

			if qtd_total_navios == 0:
				jFluxo = False

	def escolherNavioJogTeste(self,jog1 = False):
		
		dict_aux = self.criarDictNavioValor()

		navioAtual = 0;
		qtd_navio_aux = 0;

		if not jog1:
			
			#PORTA_AVIAO ---> 5
			abrevNavio = LISTA_CHAVES[0]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("A1-A5",navioSel)
			dict_aux[abrevNavio] -= 1
			
			#NAVIO_TANQUE ---> 4

			abrevNavio = LISTA_CHAVES[1]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("A7-A10",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("C1-C4",navioSel)
			dict_aux[abrevNavio] -= 1

			#CONTRA_TORPEDOS ---> 3

			abrevNavio = LISTA_CHAVES[2]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("C6-C8",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("D1-D3",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("D5-D7",navioSel)
			dict_aux[abrevNavio] -= 1

			#SUBMARINO ----> 2

			abrevNavio = LISTA_CHAVES[3]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("E1-F1",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("G2-H2",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("H4-I4",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j2.posicionarNavio("J8-J9",navioSel)
			dict_aux[abrevNavio] -= 1
		else:
			#PORTA_AVIAO ---> 5
			abrevNavio = LISTA_CHAVES[0]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("A1-A5",navioSel)
			dict_aux[abrevNavio] -= 1
			
			#NAVIO_TANQUE ---> 4

			abrevNavio = LISTA_CHAVES[1]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("A7-A10",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("C1-C4",navioSel)
			dict_aux[abrevNavio] -= 1

			#CONTRA_TORPEDOS ---> 3

			abrevNavio = LISTA_CHAVES[2]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("C6-C8",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("D1-D3",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("D5-D7",navioSel)
			dict_aux[abrevNavio] -= 1

			#SUBMARINO ----> 2

			abrevNavio = LISTA_CHAVES[3]

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("E1-F1",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("G2-H2",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("H4-I4",navioSel)
			dict_aux[abrevNavio] -= 1

			navioSel,validezInput = self.selecionarNavio(abrevNavio,dict_aux)	
			resultEsperado = self.j1.posicionarNavio("J8-J9",navioSel)
			dict_aux[abrevNavio] -= 1



	def jogadaJogador1(self):
		#...
		j1Fluxo = True

		while j1Fluxo:
			print("===================VEZ DO JOGADOR 1:==============================")
			self.estadoJogo(MSG_JOG1)
			print("----------------------------------------------------------------------------------------------------")
			posTiro = input("Digite a posição de ataque ao seu oponente.\nEX: A1, B4, J10\n----------------------------------------------------------------------------------------------------\n")
			validezInputPos = self.verificarValidezPosicao(posTiro)

			if validezInputPos:
				opSuccs,acertouNav,navAbatido = self.j1.atacarOponente(self.j2,posTiro)

				if not opSuccs: #Posição já atacada
					print("POSIÇÃO JÁ ESCOLHIDA. POR FAVOR, SELECIONE OUTRA\n")
					continue

				if opSuccs and acertouNav and not navAbatido:
					print("NAVIO ATINGINDO! POR FAVOR, JOGUE NOVAMENTE!")
					continue

				if opSuccs and acertouNav and navAbatido:
					print("NAVIO DESTRUÍDO! POR FAVOR, JOGUE NOVAMENTE!")
					opSuccs,jog1Venceu,jog2Venceu = self.fimJogo()
					if opSuccs:
						if jog1Venceu: #jogador 1 venceu!
							print("=====================================================")
							print("JOGADOR 1 FOI O VENCENDOR! :)")
							print("=====================================================")
							return True
							#break

					print("Tiro Jogador 1: ", posTiro)
					continue		
			else:
				print("POSIÇÃO INVÁLIDA. POR FAVOR, SELECIONE OUTRA\n")
				continue
			
			j1Fluxo = False

			print("JOGADA DO JOGADOR 1 EFETUADA!\n")

		return False


	def jogadaJogador2(self,jogadorMaquina = False):
		#...
		j2Fluxo = True

		if jogadorMaquina:
			print("===================VEZ DO JOGADOR 2:==============================")
			while j2Fluxo:
				posTiro = self.selecaoJogadorMaquinaTiro()
				validezInputPos = self.verificarValidezPosicao(posTiro)

				if validezInputPos:
					opSuccs,acertouNav,navAbatido = self.j1.atacarOponente(self.j1,posTiro)

					if not opSuccs: #Posição já atacada
						continue

					if opSuccs and acertouNav and not navAbatido:
						print("Tiro Jogador 2: ", posTiro)
						continue

					if opSuccs and acertouNav and navAbatido:
						opSuccs,jog1Venceu,jog2Venceu = self.fimJogo()
						if opSuccs:
							if jog2Venceu: #jogador 2 venceu!
								print("=====================================================")
								print("JOGADOR 2 FOI O VENCENDOR! :)")
								print("=====================================================")
								return True
								#break

						print("Tiro j2: ", posTiro)
						continue	
				else:
					continue

				print("Tiro Jogador 2: ", posTiro)
				j2Fluxo = False
		else:
			while j2Fluxo:
				#Vez jogador 2
				print("===================VEZ DO JOGADOR 2:==============================")
				self.estadoJogo(MSG_JOG2)
				print("----------------------------------------------------------------------------------------------------")
				posTiro = input("Digite a posição de ataque ao seu oponente.\nEX: A1, B4, J10\n----------------------------------------------------------------------------------------------------\n")
				validezInputPos = self.verificarValidezPosicao(posTiro)

				if validezInputPos:
					opSuccs,acertouNav,navAbatido = self.j1.atacarOponente(self.j1,posTiro)

					if not opSuccs: #Posição já atacada
						print("POSIÇÃO JÁ ESCOLHIDA. POR FAVOR, SELECIONE OUTRA\n")
						continue

					if opSuccs and acertouNav and not navAbatido:
						print("NAVIO ATINGINDO! POR FAVOR, JOGUE NOVAMENTE!")
						print("Tiro Jogador 2: ", posTiro)
						continue

					if opSuccs and acertouNav and navAbatido:
						print("NAVIO DESTRUÍDO! POR FAVOR, JOGUE NOVAMENTE!")
						opSuccs,jog1Venceu,jog2Venceu = self.fimJogo()
						if opSuccs:
							if jog2Venceu: #jogador 2 venceu!
								print("=====================================================")
								print("JOGADOR 2 FOI O VENCENDOR! :)")
								print("=====================================================")
								return True
								#break

						print("Tiro j2: ", posTiro)
						continue	
				else:
					print("POSIÇÃO INVÁLIDA. POR FAVOR, SELECIONE OUTRA\n")
					continue

				print("Tiro Jogador 2: ", posTiro)
				j2Fluxo = False


		print("JOGADA DO JOGADOR 2 EFETUADA!\n")
		return False

    #msgJog: Uma string que será enviada do cliente jogador até o server para identificar qual estado enviar.
    #msgs: "Jog1" ou "Jog2"
    #visJogador: Se o método é solicitado para executar em um server Observador ou não.
	def estadoJogo(self,msgJog,visJogador=True):
		posx = 0
		posy1 = 0
		posy2 = 0
		c = 0
		c2 = 0
		count_letter = 0
		j = 0
		a = 0
		print("\t",end="")

		if visJogador and msgJog == MSG_JOG1:
			print("#Jogador:","\t\t","#Oponente:")
		elif visJogador and msgJog == MSG_JOG2:
			print("#Oponente:","\t\t","#Jogador:") 
		else:
			print("#Jogador 1:","\t\t","#Jogador 2:")

		print("\t",end="")

		for i in range(0,TAM_PADRAO):
			print(i+1,end=" ")

		print("\t"," ",end="")

		for i in range(0,TAM_PADRAO):
			print(i+1,end=" ")

		print()

		print("\t",end="")

		for i in range(0,TAM_PADRAO):
			print("-",end=" ")

		print("\t"," ",end="")

		for i in range(0,TAM_PADRAO):
			print("-",end=" ")

		#for i in range(0,TAM_PADRAO**2):
		while a < TAM_PADRAO**2:
			if c % TAM_PADRAO == 0:

				#for j in range(0,TAM_PADRAO):
				while j < TAM_PADRAO:
					if c2 % TAM_PADRAO == 0:
						print()
						print("    ",LETRAS_TABULEIRO[count_letter],"|",end="")
						count_letter += 1

					c2 += 1

					if not visJogador or msgJog == MSG_JOG1:
						print(self.__j1.tabuleiro.tabMatriz[posx,posy1], end=" ")
					else:
						if self.__j1.tabuleiro.tabMatriz[posx,posy1] == NUM_NAVIO_TABULEIRO: 
							print(NUM_VAZIO_TABULEIRO, end=" ")
						else:
							print(self.__j1.tabuleiro.tabMatriz[posx,posy1], end=" ")	


					posy1 += 1
					j += 1

				print("  ",LETRAS_TABULEIRO[count_letter-1],"|",end="")
				posx += 1
				posy1 = 0;
				posy2 = 0;
				j = 0

			if not visJogador or msgJog == MSG_JOG2:
				print(self.__j2.tabuleiro.tabMatriz[posx-1,posy2], end=" ")
			else:
				if self.__j2.tabuleiro.tabMatriz[posx-1,posy2] == NUM_NAVIO_TABULEIRO: 
					print(NUM_VAZIO_TABULEIRO, end=" ")
				else:
					print(self.__j2.tabuleiro.tabMatriz[posx-1,posy2], end=" ")

			c += 1
			posy2 += 1
			a += 1

		print("\n")
		print("Legenda:","\n",str(NUM_VAZIO_TABULEIRO)," -> Disponível","\n",str(NUM_TIRO_TABULEIRO)," -> Atingido","\n",str(NUM_NAVIO_TABULEIRO)," -> Posição dos navios","\n",NUM_NAVIO_TIRO_TABULEIRO," -> Navio atingido\n")
		print("Quantidade de Navios Jogador 1: ", str(len(self.__j1.navios)), "\nQuantidade de Navios Jogador 2: ",str(len(self.__j2.navios)))


	def verificarValidezPosicao(self,input):

		if len(input) > 0:
			if input[0].upper() in LETRAS_TABULEIRO: #s.ascii_letters: #Começa com letra

				if input[1:].isdigit() and (int(input[1:]) >= 1 and int(input[1:]) <= TAM_PADRAO):
					return True
				else:
					return False
			else:
				return False		


	def verificarValidezInputPosicaoNavio(self,pos): #pos -> string

		delimiter = pos.find('-')

		if delimiter >= 2 and len(pos) >= 5: #5 é o tamanho mínimo da string válida.
			if self.verificarValidezPosicao(pos[0:delimiter]) and self.verificarValidezPosicao(pos[delimiter+1:]):

				if (pos[0].upper() > pos[pos.find('-')+1].upper()) or (int(pos[1:pos.find('-')]) > int(pos[pos.find('-')+2:])):
					return False
				elif int(pos[1:pos.find('-')]) <= 0 or int(pos[pos.find('-')+2:]) > TAM_PADRAO:
					return False
				else:
					return True
			else:
				return False
		else:
			return False

	def apresentacao(self):
		print("====================================================")
		print("BEM-VINDO AO JOGO BATALHA NAVAL!\n\nINFORMACOES DO JOGO:\n\nTAMANHO TABULEIRO:",str(TAM_PADRAO) + "x" + str(TAM_PADRAO),"\nLETRAS: " + LETRAS_TABULEIRO[0] + "-" + LETRAS_TABULEIRO[TAM_PADRAO-1] + " --> Linhas" +"\nNUMEROS: 1-" + str(TAM_PADRAO) + " --> Colunas")
		print("====================================================\n\n")

	def fimJogo(self):
		if len(self.__j1.navios) == 0:
			return (True,False,True)

		if len(self.__j2.navios) == 0:
			return (True,True,False)

		return (False,False,False)
