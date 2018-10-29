# 03 an informal introduction to python

# 3.1.1 NUMBERS
# uma divisão com / sempre retorna um numero tipo FLOAT
# mas podemos retorna-la como int usando // 
# para calcular o resto, utilizamos %

print(17/2, 17//2, 17%2)

# é possível utilizar ** para elevar um número a algo

print(12**2)

# para atribuir valor a uma variável, usamos =

variable_1 = (17**2)
print(variable_1)

# 3.1.2 STRINGS
# para criar uma string, utilizamos '', se quisermos utilizar ' dentro da string,
# utilizamos \', assim não a fecharemos

print('É isso aí mesmo.')
print('É isso a\'í mesmo.')

# characters que antes possuem \ são especiais, se quiser que não seja, utilize uma raw string

print('Primeira linha \nSegunda linha')
print (r'Primeira linha \nSegunda linha')

# strings podem ocupar varias linhas, com '''
# os finais de cada linha são inclusos automaticamente,
# mas isso pode ser evitado utilizando \ no fim da linha

print("""\
Olá amiguinho!
    Vamos aprender python hoje!
É um prazer te conhecer!
""")
print("""
Olá amiguinho!
    Vamos aprender python hoje!
É um prazer te conhecer!
""")

# strings também podem ser concatenadas
# duas ou mais strings literais perto uma da outra são automaticamente concatenadas
python = 'Py' + 'thon'
print(python)

text = ('Podemos colocar várias strings entre parenteses,'
        ' então, elas irão se juntar desse jeito.')
print(text)

# para concatenar strings e variáveis utilize +
prefix = 'Py'
print(prefix + 'thon')

# strings podem ser indexadas
# podemos pegar seu primeiro index com [0], e assim por diante
# podemos também começar a pegar da direita pra esquerda, começando com [-1]
# pode se também fazer slicing em python, pegando de uma letra ate outra que voce quer,
# por exemplo, podemos utilizar [0:4] para pegar 'Pyth' (o último index é excluído)
# a função len() retorna o tamanho da string
word = "Python"
primeira_letra = word[0] 
primeira_letra_denovo = word[-6]
ultima_letra = word[5]
ultima_letra_denovo = word[-1]
print(primeira_letra + " " + ultima_letra)
print(primeira_letra_denovo + " " + ultima_letra_denovo)
print(word[0:4])
print(len(word))

# 3.1.3 - LISTAS
# o python tem varios tipo de dados compostos, utilizados para agrupar valores
# o mais utilizado é a lista, uma lista pode conter diversos itens
# a função len() também se aplica em listas
lista_de_quantas_vezes_eu_ja_me_fudi = [1, 9, 25, 78, 108, 156]
print(lista_de_quantas_vezes_eu_ja_me_fudi)
len(lista_de_quantas_vezes_eu_ja_me_fudi)

# também podemos utilizar indexes com listas, por exemplo
primeiro_numero = lista_de_quantas_vezes_eu_ja_me_fudi[0]
segundo_numero = lista_de_quantas_vezes_eu_ja_me_fudi[1]
todos_os_numeros_depois_do_segundo_menos_o_ultimo = lista_de_quantas_vezes_eu_ja_me_fudi[1:5]
print(primeiro_numero, segundo_numero)
print(todos_os_numeros_depois_do_segundo_menos_o_ultimo)

# listas tambem suportam concatenação

print(lista_de_quantas_vezes_eu_ja_me_fudi + [11, 12, 13, 14, 15])

# diferente das strings, as listas sao mutaveis, entao podemos
# por exemplo, trocar um dos valores a partir do index

lista_de_quantas_vezes_eu_ja_me_fudi[0] = 9999999
print(lista_de_quantas_vezes_eu_ja_me_fudi)

# para adicionar novos itens em uma lista, usamos append

lista_de_quantas_vezes_eu_ja_me_fudi.append(9999 * 3)
print(lista_de_quantas_vezes_eu_ja_me_fudi)

# podemos ate mesmo remover alguns campos da lista

lista_de_quantas_vezes_eu_ja_me_fudi[1:4] = []
print(lista_de_quantas_vezes_eu_ja_me_fudi)

# por ultimo, podemos usar o python para, por exemplo,
# criar uma sequencia de fibonacci

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

# aqui, atribuimos duas variaveis, e sempre printamos a
# então, a se torna b, e b se torna a + b
# podemos utilizar o end para que não se crie uma nova linha sempre
a, b = 0, 1
while a < 10:
    print(a, end=', ')
    a, b = b, a + b

    
