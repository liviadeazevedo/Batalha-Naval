from Jogo import * 

#Inicializa a partida.
partida = Jogo()

#Variáveis auxiliares para o controle do jogo.
fimJogo = False
jogadorMaquina = False
comcarJogoJ1 = False

#OBS: Caso queira realizar testes no jogo, descomente as linhas 24 ou/e 29 para gerar tabuleiros de teste (posições já pré-definidas)

#Fluxo do jogo.
while not fimJogo:
	#------------------------------Parte 1: Apresentar o jogo para o usuário------------------------------.
	partida.apresentacao()

	#------------------------------Parte 2: Jogadores escolherem e colocarem os navios nos tabuleiros------------------------------

	#Jogador 1
	print("========================POSICIONAMENTO DOS NAVIOS JOGADOR 1!========================\n")
	partida.escolherNavio(j1Vez = True)
	#partida.escolherNavioJogTeste(jog1 = True) #PARA TESTES

	#Jogador 2
	print("========================POSICIONAMENTO DOS NAVIOS JOGADOR 2!========================\n")
	partida.escolherNavio(j1Vez = False)
	#partida.escolherNavioJogTeste() #PARA TESTES

	#------------------------------Parte 3: Inicio do jogo------------------------------
	
	#Definir aleatoriamente quem começa o jogo. Escolha de um número aleatório entre 0 e 9. Se num < 5, então jogador 1 inicia, caso contrário, jogador 2 inicia.
	print("========================DEFININDO ALEATORIAMENTE QUEM INICIARÁ O JOGO!========================\n")
	escolha = randint(0,9)
	if escolha >= 5:
		print("========================QUEM COMEÇA É O JOGADOR 1!========================\n")
		comcarJogoJ1 = True
	else:
		print("========================QUEM COMEÇA É O JOGADOR 2!========================")

	#Fluxo dos ataques dos jogadores.
	if comcarJogoJ1:
		while True:	
			fimJogo = partida.jogadaJogador1() #Jogador 1 faz a jogada.

			if fimJogo: #Se o jogo acabou com a jogada do jogador 1, saia do fluxo e declare jogador 1 vencendor.
				break

			fimJogo = partida.jogadaJogador2(jogadorMaquina) #Jogador 2 faz a jogada.

			if fimJogo: #Se o jogo acabou com a jogada do jogador 2, saia do fluxo e declare jogador 2 vencedor.
				break
	else: #Caso jogador 2 comece a partida. Mesma lógica do bloca acima, apenas com a inversão da chamada dos métodos.
		while True:	
			fimJogo = partida.jogadaJogador2(jogadorMaquina)

			if fimJogo:
				break

			fimJogo = partida.jogadaJogador1()

			if fimJogo:
				break

