"""
1.Apresente uma definição da função def enum_from_to(a: int, b: int) -> List[int] 
que constrói a lista dos números inteiros compreendidos entre dois limites.
"""
def enum_from_to(a,b):
	lst = list()
	while(a <= b):
		lst.append(a)
		a += 1
	return lst

"""
2.Apresente uma definição da função def reverse(a: List[Any]) -> List[Any]
que dada uma lista calcula uma lista com os elementos dessa lista pela ordem
inversa.
"""

def reverso(lst):
	size = len(lst)
	new = list()
	for item in lst:
		size -= 1
		new.append(lst[size])
	return new

"""
3.Apresente uma definição da função def elem(a: Any, b: List[Any]) -> bool
que testa se um elemento existe numa lista.
"""

def elem(x, lst):
	ans = False
	for i in lst:
		if i == x: ans = True
	return ans

"""
4.Apresente uma definição da função def maximo(a: List[int]) -> int
que, dada uma lista de inteiros, devolve o maior elemento dessa lista.
"""

def maximo(lst):
	maior = lst[0]
	for item in lst:
		if item > maior: maior = item
	return maior

"""
5.Apresente uma definição da função def somas_acumuladas(a: List[int]) -> List[int]
que, dada uma lista de inteiros, devolve uma nova lista que contém as somas acumuladas da lista original.
"""

def soma_acumuladas(lst):
	total = 0
	new = list()
	for item in lst:
		total += item
		new.append(total)
	return new