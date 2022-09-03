nomes = open("names.txt", "r")
nomes = nomes.read()
def transform_lista(a):
    x = a.split(",")
    return x
def remove_aspas(b):
    return b.replace('"', "")


        
ordem_alfa = sorted(transform_lista(remove_aspas(nomes)))
cont = 0
valor_total = 0
for i in range(len(ordem_alfa)):
    for letter in ordem_alfa[i]:
        cont += ord(letter)-64
    valor_total += cont * i
print(i)
        

