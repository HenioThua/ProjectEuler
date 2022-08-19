m = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
def maior(m, i, j):
    return m[i][j]

def max_soma(m, i, j):
    soma = 0
    maior = 0
    if i == len(m)-1:
         return m[i][j]
    elif i == len(m) -2:
        return m[i][j] + max(m[i+1][j], m[i+1][j+1])

def euler_18(m):
    m_aux = refine(m)
    return m_aux[0][0]

def refine(m):
    for i in range(len(m)-1):
        ult_line = m.pop()
        penu_line= m.pop()
        line_combined = combine_line(ult_line, penu_line)
        m.append(line_combined)
    return m

def combine_line(ultima_linha, penultima_linha):
    lista_combinada = []
    for i in range(len(penultima_linha)):
        filho_esquerda = ultima_linha[i]
        filho_direita = ultima_linha[i+1]
        total = max(filho_direita, filho_esquerda) + penultima_linha[i]
        lista_combinada.append(total)
    return lista_combinada
print(euler_18(m))
        

