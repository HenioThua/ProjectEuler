fator_100 = 1
for i in range(100,0,-1):
    fator_100 = fator_100 * i
soma_digitos_fator = 0
for i in str(fator_100):
    soma_digitos_fator += int(i)
print(soma_digitos_fator)

    
