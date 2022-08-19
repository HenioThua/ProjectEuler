from math import sqrt
def inesimo(a):
    return a * (a + 1) / 2
def fator(b):
    cont = 1
    cont2 = 0
    t = sqrt(b)
    while cont < t:
        if b % cont == 0:
            cont2 += 2
        cont +=1
    if t * t == b:
        cont2 +=1 
    return cont2
cont = 1
while True:
    i = inesimo(cont)
    u = fator(i)
    if u > 500:
        print(i)
        break
    else:
        cont+=1
        

