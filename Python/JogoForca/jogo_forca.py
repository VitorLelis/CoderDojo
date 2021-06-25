from palavras import escolher_palavra
from desenhos import desenho_forca, check_display, rodada
	         
print("Bem vindo o jogo de Forca!! Selecione o nível:")
nivel = input("A -> Easy\nB -> Medium\nC -> Hard\n")
palavra = escolher_palavra(nivel)

tentativa = 0

not_letras = list()
display = list()

for i in range(len(palavra)):
	display.append('_')

print(desenho_forca(tentativa)+'\n')
control = True
while(control):
	tentativa = rodada(not_letras, palavra, display, tentativa)

	if '_' not in display:
		control = False

	elif tentativa > 5:
		control = False


if tentativa >= 5:
	print("\nForca :(\n")
else:
	print("\nParabens :)\n")

print("Ate mais!\n")