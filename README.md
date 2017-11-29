# Batalha Naval
Repositório que contém uma implementação do jogo "Batalha Naval" em Python 3.
Recomenda-se executar a aplicação via Terminal Linux.

Para executar o jogo, basta abrir pelo Terminal (no diretório onde está os arquivos do jogo) e digitar:

    python Main.py

ou, caso necessário especificar a versão do Python a ser usada:

    python3 Main.py
    
Todas as instruções para o prosseguimento do jogo estão presentes durante a execução.

### MODO DE EXECUTAR O JOGO NO SERVIDOR

Abra 4 janelas do Terminal e:
1. Em uma das janelas, execute uma instância de ServerBatalhaNaval.py.

        python3 ServerBatalhaNaval.py

2. Nas 3 janelas restantes execute, em cada uma delas, uma instância de pseudo-cliente.py, sendo a ordem **Player1 (P1)**, **Player2 (P2)** e **Observador**.

        python3 pseudo-cliente.py

3. Jogue o jogo normalmente alternando entre **P1** e **P2** para enviar as informações de acordo com o informado.
