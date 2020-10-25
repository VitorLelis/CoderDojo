"""
Funções simples para ensinar e mostrar o básico de Python

Simple functions to teach and show Python basics
"""
def input_output():
	name = input("Como se chama?\n")
	print("Ola,", name)

def listas():
	lst = [1,2,3,4]
	print(lst)
	lst.append(5)
	print(lst)
	lst.remove(3)
	print(lst)
	print(lst[1])

def condicionais():
	x = int(input("Numero:"))
	if x < 10: print("pequeno")
	elif x < 20: print("medio")
	else: print("grande")

def for_loop(n):
	for i in range(n):
		print(i)

def while_loop(n):
	while(n > 0):
		print("not yet")
		n -= 1
	print("Done!")