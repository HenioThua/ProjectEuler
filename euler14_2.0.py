cadeia_dic = {} 
def cadeia(a):
    if a not in cadeia_dic:
        if a == 1:
            cadeia_dic[a] = 1
        elif a % 2 == 0:
            cadeia_dic[a] = 1+ cadeia(a/2)
        else:
            cadeia_dic[a] =  1+ cadeia(a * 3 + 1)
    return cadeia_dic[a]
indice = 1
cadeia_max = 1
for i in range(1,1000000):
    if cadeia(i) > cadeia_max:
        cadeia_max = cadeia(i)
        indice = i
    print(indice, cadeia_max)
