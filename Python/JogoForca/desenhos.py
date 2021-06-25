def desenho_forca(tentativa):
	desenho = [
	''' 
	               --------
	               |      |
	               |      
	               |      
	               |     
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |      
	               |     
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |      | 
	               |      
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |     /| 
	               |     
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |     /|/ 
	               |     
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |     /|/ 
	               |     / 
	               |        ''',
	''' 
	               --------
	               |      |
	               |      O
	               |     /|/ 
	               |     / /
	               |        '''
	          ]

	return desenho[tentativa]

def check_display(letra, palavra, display):

	for i in range(len(palavra)):
		
		if palavra[i].lower() == letra.lower():
			display[i] = palavra[i].lower()

def rodada(not_letras, palavra, display,tentativa):
	letra = input("\nQual sua letra?\n")

	if letra.lower() in palavra.lower():
		check_display(letra, palavra, display)
	else:
		not_letras.append(" "+letra.lower())
		tentativa += 1

	print(desenho_forca(tentativa)+'\n')
	print("Letras erradas: "+' '.join(not_letras)+"\n")
	print(' '.join(display))

	return tentativa