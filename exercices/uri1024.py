linha = int(input())
lista_string = []

for i in range (0, linha):
    texto = input()
    lista_string.append(texto)

print(lista_string)

for i in range (0, linha):
    palavra = list(lista_string[i])

    for letra in palavra:
        if letra.isalpha():
            letra = chr(ord(palavra[i]) + 3)
    print(letra)

'''for i in range (0, len(lista_string)):
    for i in range(0, len(lista_string[i]))
        if lista_string[i].isalpha():
            lista_string[i] = chr(ord(lista_string[i]) + 3)

print(lista_string)'''



