import random
"""
Ideia para o projeto do jogo de Pedra, Papel e Tesoura em Python

Rock, Paper and Scissors game project idea on Python
"""

"""
Função que compara as 2 jogadas para determinar o vencedor

Function to compare the 2 plays and determine the winner
"""
def comparar_jogadas(jog1,jog2):
	if jog1 == jog2: return "Empate"
	else:
		if (jog1 == 0 and jog2 == 2) or (jog1 == 1 and jog2 == 0) or (jog1 == 2 and jog2 == 1): return "Venceu"
		else: return "Perdeu"

"""
Modo de partidas infinitas que corre até o Ninja escolher a opção de sair(3)

Infinite matches mode that run's until the Ninja chooses the exit option(3)
"""

def modo_1():
	jogadas = ["Pedra", "Papel", "Tesoura"]
	while(True):
		print("\n0->Pedra\n1->Papel\n2->Tesoura\n3->Sair\n")
		jogNinja = int(input("Qual a sua jogada?\n"))
	
		if jogNinja == 3: quit()
		else: jogMaquina = random.choice(range(3))
		
		print("\nNinja jogou:", jogadas[jogNinja])
		print("\nMaquina jogou:", jogadas[jogMaquina])
		resp = comparar_jogadas(jogNinja,jogMaquina)
		print(resp)

"""
Modo Guardiões, onde é impossível de vencer a Máquina. Feita para ser jogada pelos Guardiões

Guardian's mode, where is impossible to beat the Machine. Made to be played by the Guardians
"""

def modo_2():
	jogadas = ["Pedra", "Papel", "Tesoura"]
	while(True):
		print("\n0->Pedra\n1->Papel\n2->Tesoura\n3->Sair\n")
		jogGuard = int(input("Qual a sua jogada?\n"))
	
		if jogGuard == 3: quit()
		else:
			if jogGuard == 0: jogMaquina = 1
			elif jogGuard == 1: jogMaquina = 2
			elif jogGuard == 2: jogMaquina = 0

		print("\nGuardião jogou:", jogadas[jogGuard-1])
		print("\nMaquina jogou:", jogadas[jogMaquina-1])
		resp = comparar_jogadas(jogGuard,jogMaquina)
		print(resp)

"""
Modo Best of N. Conta o nº de vitórias feitas pelo Ninja e pela Máquina, até alguém chegar ao necessário para acabar

Best of N mode. Counts the number of victories made by the Ninja and the Machine, until someone reaches the needed to finish
"""

def modo_3():
	jogadas = ["Pedra", "Papel", "Tesoura"]
	
	best = int(input("Quantas partidas no max?\n"))
	best = (best+1)/2
	vitNj = 0
	vitMaq = 0

	while((vitNj < best) and (vitMaq < best)):
		print("\n0->Pedra\n1->Papel\n2->Tesoura\n")
		jogNinja = int(input("Qual a sua jogada?\n"))
	
		jogMaquina = random.choice(range(3))
		
		print("\nNinja jogou:", jogadas[jogNinja-1])
		print("\nMaquina jogou:", jogadas[jogMaquina-1])
		
		resp = comparar_jogadas(jogNinja,jogMaquina)

		if resp == "Venceu": vitNj += 1
		elif resp == "Perdeu": vitMaq += 1
		print("Ninja:", vitNj)
		print("Maquina:", vitMaq)

	if(vitNj > vitMaq): print("Ninja Venceu!!")
	else: print("Maquina venceu!!")

"""
Mensagem de abertura do jogo e seleção de modo

Game's opening message mode selection
"""

print("Pedra, Papel e Tesoura!!")
modo = int(input("1->Infinito\n2->Guardião\n3->Best of N\n"))
if modo == 1: modo_1()
elif modo == 2: modo_2()
elif modo == 3: modo_3()
