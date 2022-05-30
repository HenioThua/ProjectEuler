def mdc(n1, n2):
    if n2 == 0:
        return n1 
    return mdc (n2, n1 % n2)

def mmc (n1, n2):
    return (n1 * n2) / mdc (n1, n2)

aux = 1
for i in range(1, 21):
    aux = mmc(aux, i)
print(aux)
