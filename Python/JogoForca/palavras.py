import random

def escolher_palavra(nivel):

	easy = ['Amarelo', 'Amiga', 'Amor', 'Ave', 'Aviao', 'Avo', 'Balao', 'Bebe', 'Bolo', 
			'Branco', 'Cama', 'Telemovel', 'Clube', 'Copo', 'Doce', 'Elefante', 'Escola', 
			'Faca', 'Foto', 'Garfo', 'Girafa', 'Janela', 'Limonada', 'Mae', 'Meia', 'Noite', 'Oculos', 
			'Autocarro', 'Comboio', 'Ovo', 'Pai', 'Pao', 'Parque', 'Passaro', 'Peixe', 'Pijama', 'Rato']


	medium = ['Chocolate', 'Programacao', 'Coderdojo', 'Portugal', 'Brasil', 
			  'Cristiano', 'Ronaldo', 'Universidade', 'Informatica', 'Computador', 
			  'Portatil', 'Benfica', 'Porto', 'Sporting', 'Braga', 'Guimaraes', 'Lisboa', 'Ninja']
	
	hard =['Acender', 'Afilhado', 'Aspero', 'Assombracao', 'Asterisco', 'Basquetebol', 
		   'Badminton', 'Natacao', 'Futebol', 'Caminho', 'Chiclete', 'Coelho', 'Contexto', 'Convivencia', 
		   'Coracao', 'Hamburguer', 'Esquerdo', 'Excecao', 'Horrorizado', 'Impacto', 'Independencia', 'Modernidade', 
		   'Oftalmologista', 'Otorrinolaringologista', 'Paralelepipedo', 'Quarentena', 'Refeicao', 'Reportagem', 
		   'Sino', 'Tenue']

	if nivel.upper() == 'A':
		return random.choice(easy)
	elif nivel.upper() == 'B':
		return random.choice(medium)
	elif nivel.upper() == 'C':
		return random.choice(hard) 
