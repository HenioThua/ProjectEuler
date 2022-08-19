dic = {}
def n_rotas(i, j):
    if (i,j) in dic:
        return dic[(i,j)]
    if i == 0 and j == 0:
        dic[(i,j)] = 1
    elif j == 0:
        dic[(i,j)] = n_rotas(i-1, 0)
    elif i == 0:
        dic[(i,j)] = n_rotas(0, j-1) 
    else:
        dic[(i,j)] = n_rotas(i, j-1) + n_rotas(i-1 , j)
    return dic[(i,j)]
print(n_rotas(20, 20))
        
        
