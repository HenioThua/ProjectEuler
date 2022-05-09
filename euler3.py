maior = 0
def isPrimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = 600851475143
i = 2
while n != 1:
    if isPrimo(i) and n % i == 0:
        if maior < i:
            maior = i
        n = n / i
    else:
        i = i+1
print(maior)  
    
    
