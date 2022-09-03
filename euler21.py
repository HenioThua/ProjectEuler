def divisores(n):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores         
def eh_amigavel(j):
    soma_div_prop = divisores(j) 
    if divisores(soma_div_prop) == j and soma_div_prop != j:
        return True
    else:
        return False
soma = 0 
for i in range(1,10000):
    if eh_amigavel(i) == True:
        soma +=i 
        print(soma)
    
