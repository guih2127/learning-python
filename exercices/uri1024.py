numero_casos = int(input())
saida = []
nova_palavra = []
nova_palavra2 = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ASCII = ''.join(chr(x) for x in range(128))
ASCII = ASCII.split()
print(ASCII)

for i in range(numero_casos):
    palavra = input()
    for letra in palavra:
        if letra in letras:
            if letra == 'x':
                nova_letra = '{'
            elif letra == 'X':
                nova_letra = '['
            elif letra == 'y':
                nova_letra = '|'
            elif letra == 'Y':
                nova_letra = '\\'
            elif letra == 'z':
                nova_letra = '}'
            elif letra == 'Z':
                nova_letra = ']'
            else:
                for i in range(0, len(letras)):
                    if letra == letras[i]:
                        nova_letra = letras[i + 3]
                        break
            nova_palavra.append(nova_letra)
    
    inverter = reversed(nova_palavra)
    for letra in inverter:
        nova_palavra2.append(letra)

    tamanho_palavra = len(nova_palavra2)
    tamanho_por_dois = int(tamanho_palavra / 2) * (-1)

    for i in range(-1, tamanho_por_dois):
        for j in range(0, len(ASCII)):
            if nova_palavra2[i] == ASCII[j]:
                nova_palavra2[i] = ASCII[j - 1]

print(nova_palavra2)