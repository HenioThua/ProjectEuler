
def number_name(a):
    dic = {1:"one", 2:"two", 3:"three", 4:"four",5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    dic2= {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    dic3= {1:"eleven", 2:"twoelve", 3:"thirteen", 4:"fourteen", 5:"fiteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}
    uni = a // 1 % 10
    dez = a // 10 % 10
    cen = a // 100 % 10
    if cen == 0 and dez == 1 and uni != 0:
        return dic3[uni]
    if uni != 0 and dez == 0 and cen == 0:
        return dic[uni]
    if uni == 0  and dez != 0 and cen == 0:
        return dic2[dez]
    if uni != 0 and dez != 0 and cen == 0:
         return dic2[dez] + dic[uni]   
    if uni == 0 and dez == 0 and cen != 0:
        return dic[cen] + " hundred"
    if (uni != 0 or dez != 0) and cen != 0:
        return dic[cen] + " hundred" + " and " + number_name(dez * 10 + uni)

def remove_s(s):
    return s.replace(" ", "")

quant_letras = 0
for i in range(1,1000):
    quant_letras+= len(remove_s(number_name(i)))
print(quant_letras + 11)
    
    
    
    
    
