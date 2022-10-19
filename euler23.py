from abundantes import numeros_abundantes
def soma_div_prop(n):
    valor = 0 
    for i in range(1, n//2 +1):
        if n % i == 0:
            valor += i
    return valor
    
DEFICIENTE = -1
PERFEITO = 0
ABUNDANTE = 1

def def_perf_abund(n):
    valor = soma_div_prop(n)
    if valor == n:
        return PERFEITO
    elif valor > n:
        return ABUNDANTE
    else:
        return DEFICIENTE

numeros_abundantes = []
def is_abundante(x):
    if def_perf_abund(x) == ABUNDANTE:
        numeros_abundantes.append(x)
    return numeros_abundantes

for i in range(1,28124):
    is_abundante(i)
    
print(is_abundante(i))
    

def is_abundante(x):
    return def_perf_abund(x) == ABUNDANTE

def canBeWrittenAsSumOfAbundantNumbers(n):
    for i in numeros_abundantes:
        if i >= n:
            break
        if n - i in numeros_abundantes:
            return True
    return False
numeros_que_nao_somam = 0 
for i in range(1,28134):
    if not canBeWrittenAsSumOfAbundantNumbers(i):
        numeros_que_nao_somam += i 
print(numeros_que_nao_somam)

