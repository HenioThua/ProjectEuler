def cadeia(a):
    cont = 1
    while a !=1:
        if a % 2 == 0:
            a = a/2
        else:
            a = a * 3 + 1
        cont += 1
    return cont
indice = 1
cadeia_max = 1
for i in range(1,1000000):
    if cadeia(i) > cadeia_max:
        cadeia_max = cadeia(i)
        indice = i
    print(indice, cadeia_max)
