from Jogo import * 
from ConexaoTCPserver import *
    
fimJogo = False
jogadorMaquina = False
comcarJogoJ1 = False

#Inicializa a partida.
partida = Jogo()

conexao = TCPconnetion()

#Fluxo do jogo.
while not fimJogo:

	msg = partida.apresentacao()
	conexao.enviarTodos(msg)
	#------------------------------Parte 2: Jogadores escolherem e colocarem os navios nos tabuleiros------------------------------

    #Jogador 1
	msg = "========================POSICIONAMENTO DOS NAVIOS JOGADOR 1!========================\n"
	conexao.enviarTodos(msg)
	print(msg)

	partida.escolherNavio(j1Vez = True, comSocket=True, conexao=conexao)
	#partida.escolherNavioJogTeste(jog1 = True) #PARA TESTES

	#Jogador 2
	msg = "\n========================POSICIONAMENTO DOS NAVIOS JOGADOR 2!========================\n"
	conexao.enviarTodos(msg)
	print(msg)
	partida.escolherNavio(j1Vez = False, comSocket=True, conexao=conexao)
	#partida.escolherNavioJogTeste() #PARA TESTES

	#------------------------------Parte 3: Inicio do jogo------------------------------
	
	#Definir aleatoriamente quem começa o jogo. Escolha de um número aleatório entre 0 e 9. Se num < 5, então jogador 1 inicia, caso contrário, jogador 2 inicia.
	msg = "\n========================DEFININDO ALEATORIAMENTE QUEM INICIARA O JOGO!========================\n\n\n"
	conexao.enviarTodos(msg)
	print(msg)
    
	escolha = randint(0,9)
	if escolha >= 5:
		msg = "========================QUEM COMECA EH O JOGADOR 1!========================\n\n\n\n"
		comcarJogoJ1 = True
	else:
		msg = "========================QUEM COMECA EH O JOGADOR 2!========================\n\n\n\n"

	conexao.enviarTodos(msg)
	print(msg)

	#Fluxo dos ataques dos jogadores.
	if comcarJogoJ1:
        
		while True:	
			fimJogo = partida.jogadaJogador1(comSocket=True,conexao=conexao) #Jogador 1 faz a jogada.

			if fimJogo: #Se o jogo acabou com a jogada do jogador 1, saia do fluxo e declare jogador 1 vencendor.
				break

            #will: a princípio o server nunca será um jogador ... o jogo só começa quando houver 2 jogadores
			fimJogo = partida.jogadaJogador2(jogadorMaquina,comSocket=True,conexao=conexao) #Jogador 2 faz a jogada.

			if fimJogo: #Se o jogo acabou com a jogada do jogador 2, saia do fluxo e declare jogador 2 vencedor.
				break
	else: #Caso jogador 2 comece a partida. Mesma lógica do bloca acima, apenas com a inversão da chamada dos métodos.
		while True:	
			fimJogo = partida.jogadaJogador2(jogadorMaquina,comSocket=True,conexao=conexao)

			if fimJogo:
				break

			fimJogo = partida.jogadaJogador1(comSocket=True,conexao=conexao)

			if fimJogo:
				break
                


conexao.fecharConexao()