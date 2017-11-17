from Jogo import * 

partida = Jogo()

fimJogo = False
jogadorMaquina = False
comcarJogoJ1 = False

while not fimJogo:
	partida.apresentacao()

	#-------Colocar os navios nos tabuleiros-----------

	#Jogador 1
	print("========================POSICIONAMENTO DOS NAVIOS JOGADOR 1!========================\n")
	partida.escolherNavio(j1Vez = True)
	#partida.escolherNavioJogTeste(jog1 = True)

	#Jogador 2
	print("========================POSICIONAMENTO DOS NAVIOS JOGADOR 2!========================\n")
	partida.escolherNavio(j1Vez = False)
	#partida.escolherNavioJogTeste()

	#-------Inicio do jogo-----------------------------
	
	#Definir aleatoriamente quem começa o jogo.
	print("========================DEFININDO ALEATORIAMENTE QUEM INICIARÁ O JOGO!========================\n")
	escolha = randint(0,9)
	if escolha >= 5:
		print("========================QUEM COMEÇA É O JOGADOR 1!========================\n")
		comcarJogoJ1 = True
	else:
		print("========================QUEM COMEÇA É O JOGADOR 2!========================")

	if comcarJogoJ1:
		while True:	
			fimJogo = partida.jogadaJogador1()

			if fimJogo:
				break

			fimJogo = partida.jogadaJogador2(jogadorMaquina)

			if fimJogo:
				break
	else:
		while True:	
			fimJogo = partida.jogadaJogador2(jogadorMaquina)

			if fimJogo:
				break

			fimJogo = partida.jogadaJogador1()

			if fimJogo:
				break

