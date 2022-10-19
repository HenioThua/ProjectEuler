contador = 0
maior = 0
while contador < 1001:
	for i in range(1,11):
		if contador / i > maior:
			maior = contador
	contador += 1
print(maior)
