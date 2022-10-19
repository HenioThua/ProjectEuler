def numeros_digitos(x):
	contador_de_digitos = 1
	while x >= 10:
		x = x // 10 
		contador_de_digitos +=1 
	return contador_de_digitos
a = 1 
b = 1
cont = 1
while numeros_digitos(a) < 1000:
	a,b = b, a+b
	cont += 1
print(cont)