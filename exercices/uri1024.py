numero_casos = int(input())
saida = []

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

standard_ascii = [chr(i) for i in range(128)]

for i in range(numero_casos):
    palavra = input()
    nova_palavra = []
    nova_palavra2 = []
    for letra in palavra:
        if letra not in letras:
            nova_letra = letra
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

        nova_palavra.append(nova_letra)
    
    for letra in reversed(nova_palavra):
        nova_palavra2.append(letra)
    
    x = round((len(nova_palavra2) / 2))

    for i in range(1, (x+1)):
        for j in range(0, len(standard_ascii)):
            if nova_palavra2[-i] == standard_ascii[j]:
                nova_palavra2[-i] = standard_ascii[j - 1]

    palavra_cript = ''.join(nova_palavra2)

    saida.append(palavra_cript)

for l in saida:
    print(l)