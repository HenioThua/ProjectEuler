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
    

        
    
