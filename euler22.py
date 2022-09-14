letters = set()
nomes = open("names.txt", "r")
nomes = nomes.read()
def transform_lista(a):
    x = a.split(",")
    return x
def remove_aspas(b):
    return b.replace('"', "")

def remove_new_line(t):
    return t.replace("\n", "")

def calc_alfa_value(r):
    cont = 0
    for i in r:
        if i == "\n":
            print(r, "tem \\n")
        letters.add(i)
        cont += ord(i) - 64
    return cont
     
ordem_alfa = sorted(transform_lista(remove_new_line(remove_aspas(nomes))))
cont = 0 
valor_total = 0
for i in range(len(ordem_alfa)):
    valor_total += calc_alfa_value(ordem_alfa[i]) * (i+1)
print(valor_total)

assert calc_alfa_value("COLIN") == 53
assert ordem_alfa[937] == "COLIN"



