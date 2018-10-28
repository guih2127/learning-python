# para criar uma função, utilizamos o def e passamos argumentos,
# como digo anteriormente.
# porem, podem existir situações nas quais não sabemos o número
# de argumentos de que uma função terá.
# por ex. uma função que calcule a soma de n numeros:

def soma(*nums):
    soma_num = 0
    
    for num in nums:
        soma_num += num

    return soma_num

# ao colocarmos o * antes de definirmos os argumentos, dizemos ao python
# que não sabemos o numero de argumentos que o usuário irá passar.
# ao fazermos isso, o python pega os argumentos passados e joga numa tupla.
# o python APENAS ACEITA um argumento com * quando ele for o ULTIMO argumento 
# da função. não podemos definir um argumento depois de um argumento variável.

# podem existir também, situações onde é preciso de argumentos bem definidos
# junto com argumentos pré-definidos, por exemplo:

def media(p1, p2, p3, peso1, peso2, peso3):
    return (p1*peso1 + p2*peso2 + p3*peso3) / soma(peso1, peso2, peso3)

print(media(5, 5, 5, 1, 1, 1))

# pode ser que, ao utilizarmos essa função, os pesos das notas das provas sejam
# todos os mesmos, o que é absolutamente normal em escolas e faculdade.
# para não ficar repetindo os argumentos (ex: 1, 1, 1), podemos deixá-los 
# predefinidos.

def media(p1, p2, p3, peso1 = 1, peso2 = 1, peso3 = 1):
    return (p1*peso1 + p2*peso2 + p3*peso3) / soma(peso1, peso2, peso3)

print(media(5, 5, 5, 1, 1, 1))

# ou seja, os valores serão informados e, caso não forem, os valores padrão
# serão peso1 = 1, peso2 = 1 e peso3 = 1.
# o python APENAS ACEITA argumentos predefinidos como os ULTIMOS argumentos
# da função, igualmente quando utilizamos o * para argumentos variáveis.

