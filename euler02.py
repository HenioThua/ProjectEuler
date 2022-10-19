a = 1
b = 2
solucao = 0
while b < 4000000:
    if b % 2 == 0:
        solucao += b
    a,b= b, a+b
print(solucao)
