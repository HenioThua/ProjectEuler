from itertools import permutations

def enesima(iterador, index):
	cont = 1
	for i in iterador:
		if cont == index:
			return i 
		else:
			cont += 1
digits = [0,1,2,3,4,5,6,7,8,9]
permutacoes = permutations(digits)
print(enesima(permutacoes, 1000000))