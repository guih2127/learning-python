# já vimos que ao passarmos uma variável como argumento 
# para uma função, passamos uma CÓPIA dele, não alterando-o diretamente.
# porém, o que acontece se passarmos uma lista para a função?

def modificar_lista(a):
    a[0] += 10

a = [1, 2, 3, 4]

modificar_lista(a)
print(a)

# a lista foi modificada mesmo fora da função.

# ex. de uma função que constroi uma matriz multidimensional em python:
matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constroi_matriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i-%i da matriz: " %(i, j)))
            linha.append(x)
        
        matriz.append(linha)

constroi_matriz(m, n, matriz)
print(matriz)

# ex. de uma função que troca elementos da matriz
def troca_elemento(posicao1, posicao2, posicao3, posicao4, matriz):
    elemento1 = matriz[posicao1 - 1][posicao2 - 1]
    elemento2 = matriz[posicao3 - 1][posicao4 - 1]
    matriz[posicao1 - 1][posicao2 - 1] = elemento2
    matriz[posicao3 - 1][posicao4 - 1] = elemento1

posicao1 = int(input("Digite o numero da linha do elemento1 a ser trocado: "))
posicao2 = int(input("Digite o numero da coluna do elemento1 a ser trocado: "))
posicao3 = int(input("Digite o numero da coluna do elemento2 a ser trocado: "))
posicao4 = int(input("Digite o numero da coluna do elemento2 a ser trocado: "))

troca_elemento(posicao1, posicao2, posicao3, posicao4, matriz)

print(matriz)

# ex. de uma função que gera uma matriz 4x4 com numeros de 0 a 15 sem repetir

import random
matriz = []

def gerar_matriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x) # remove o numero adicionado da lista de aleatorios
        matriz.append(linha)

matriz = []

gerar_matriz(matriz)
print(matriz)
