from guizero import App, Box, PushButton, Text
"""
Ideia para o Jogo da Velha usando GUI

Idea for Tic Tac Toe using GUI
"""

"""
Função que cria um novo tabuleiro vazio em formato "grid" e com os botões interativos sendo as casas para jogar

Function that creates a new  empty board in a "grid" shape and with interactive buttons being the squares to play
"""

def novo_jogo():
	novo_casas_do_tab = [[None,None,None],[None,None,None],[None,None,None]]
	for x in range(3):
		for y in range(3):
			casa = PushButton(tabuleiro, text = "", grid = [x,y], width = 9,height = 4, command = jogada, args = [x,y])
			novo_casas_do_tab[x][y] = casa

	return novo_casas_do_tab

"""
Função que realiza as jogadas da seguinte forma: 

-> Atribui o valor que está na variável global "turn" na casa jogada
->Desabilita a casa para não ser jogada novamente
-> Aumenta a quantidade de movimentos feitos representado na variável global "movs"
->Alterna o valor de "turn" para trocar o atual jogador

Function that performs the moves as follows:

-> Assign the value that is in the global variable "turn" on the house
-> Disables the house so it won't be played again
-> Increases the amount of movements made represented in the global variable "movs"
-> Toggles the "turn" value to change the current player
"""

def jogada(x,y):
	global turn
	global movs

	casas_do_tab[x][y].text = turn
	casas_do_tab[x][y].disable()
	movs += 1

	if turn == "O": turn = "X"
	else: turn = "O"
	mensagem.value = "É a vez de " + turn

	checar_vitoria(x,y)

"""
Função para conferir se houve vitória de algum jogador ou empate:
-> Checa se há na horizontal, vertical ou diagonal a repetição da mesma jogada, ou seja, a vitória de um jogador
-> Caso não haja e foram feitos todos movimentos possíveis, no caso 9, será empate

Function to check if a player has won or it is a Tie:
-> Check if there is a repetition of the same move horizontally, vertically or diagonally, that is, the victory of a player
-> If there is not and all possible moves have been made, in case 9, it will be a Tie
"""

def checar_vitoria(x,y):
	vencedor = None

	if casas_do_tab[0][y].text == casas_do_tab[1][y].text == casas_do_tab[2][y].text:
		vencedor = casas_do_tab[0][y].text

	elif casas_do_tab[x][0].text == casas_do_tab[x][1].text == casas_do_tab[x][2].text:
		vencedor = casas_do_tab[x][0].text

	elif casas_do_tab[0][0].text == casas_do_tab[1][1].text == casas_do_tab [2][2].text:
		vencedor = casas_do_tab[0][0].text

	elif casas_do_tab[0][2].text == casas_do_tab[1][1].text == casas_do_tab [2][0].text:
		vencedor = casas_do_tab[0][2].text

	if vencedor != None and vencedor in ["X","O"]: 
		mensagem.value = vencedor + " venceu!\n"
		tabuleiro.disable()

	elif movs == 9: 
		mensagem.value = "Empate!\n"
		tabuleiro.disable()

"""
Definições inicias para o jogo

Game's initial settings
"""

app = App("Tic-Tac-Toe")
app.bg ="#052c6b"

tabuleiro = Box(app, layout = "grid")

turn = "O"

movs = 0

casas_do_tab = novo_jogo()

mensagem = Text(app, text = "É a vez de "+turn)
mensagem.text_size = 20
mensagem.font = "Times New Roman"

app.display()