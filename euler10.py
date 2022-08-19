from math import sqrt
def isPrimo(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
n = 2000000
soma = 2 
for i in range(3, n, 2):
    if isPrimo(i):
        soma += i
        print(i)
print(soma)

    
