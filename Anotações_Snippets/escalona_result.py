def mult(matrix, n):
    return [[element * n for element in line] for line in matrix]


#!/usr/bin/env python3

def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def sub(m1, m2):
    matriz_sub = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_sub
        matriz_sub.append([])
        for j in range(quant_colunas):
            # subtraindo os elementos que possuem o mesmo índice
            sub = m1[i][j] - m2[i][j]
            matriz_sub[i].append(sub)
    return matriz_sub


def mult_escalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

pontos = [(200,200),(300,100),(400,200)]
pontos_medio = [(900/3,500/3),(900/3,500/3),(900/3,500/3)]
escala = 0.5

#print(mult(sub(pontos, pontos_medio), escala))
#print(mult_escalar(sub(pontos, pontos_medio), escala))
#print(pontos_medio)
print(somar(mult_escalar(sub(pontos, pontos_medio), escala),pontos_medio))
#print(sub(pontos, pontos_medio))

