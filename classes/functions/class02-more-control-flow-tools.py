# 4 . MORE CONTROL FLOW TOOLS

# acabamos de apresentar o while, mas python também conhece os usuais
# tipos de controle de fluxo conhecidos de outras linguagens


# 4.1 - IF STATEMENTS:

x = 10

if x < 0:
    x = 0
    print("Negativo mudou pra zero.")
elif x == 0:
    print("Zero.")
else:
    print("Que.") # <-

# podem haver zero ou mais elif, que se equivale a um "else if"
# uma sequencia de if, elif, elif.. substitui os switch e case
# de outras linguagens.

# 4.2 - FOR STATEMENTS:
# o for muda um pouco, no python, o for passa pelos itens de qualquer
# sequencia (como lista ou string) na ordem que eles aparecem na
# sequencia. funciona assim:

words = ['cat', 'window', 'black']

for w in words:
    print(w, len(w))

# se precisar modificar a sequencia dentro do loop, é recomendável
# criar uma copia antes, iterar em uma sequencia nao cria uma cópia
# implicitamente. o slice permite que isso seja feito:

for w in words[:]: # faz um loop em uma copia da lista
    if len(w) > 4:
        words.insert(0,w) # insere na lista os w com len > 4, no index 0

print(words)

# se nao utilizassemos o [:] aqui, criariamos uma lista infinita 

# 4.3 - THE RANGE() FUNCTION:
# se for necessario iterar uma sequencia de numeros, a funcao range()
# serve bem. ela gera progressões aritméticas:

for i in range(5):
    print(i)

for i in range(0, 20):
    print(i)

# para iterar os index de uma sequencia, pode se combinar range() e len()

for i in range(len(words)):
    print(i, words[i])

# porem, mais pra frente, iremos ver sobre tecnicas de loop.
# de varios modos, podemos pensar que o objeto retornado pela funcao range() se comporta como uma lista,
# mas na verdade, nao. range() retorna um objeto que retorna itens sucessivos em uma sequencia desejada
# quando voce o itera, mas isso nao faz dele uma lista, salvando, entao, espaço.

print(range(10)) # nao retorna uma lista

# o objeto retornado no for é ITERABLE (iterável), ou seja, pode ser uma alvo de funções que esperem algo pelos quais
# possam obter itens sucessivos até que o fornecedor se exauste. o FOR é um ITERATOR (iterador), e LIST() também,
# pois ambos criam objetos iteráveis.

# 4.4 - BREAK AND CONTINUE STATEMENTS, AND ELSE CLAUSES ON LOOPS:
# o break funciona igual em outras linguagens, ele serve pra sair de um loop
# obs: voce pode usar um ELSE para um FOR, o ELSE sera executado caso ele
# não identifique nada na lista, com O FOR, ou quando a condição for false,
# no WHILE.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# o else aqui, utilizado junto com um for, parece mais um else utilizado 
# com um TRY, do que com um IF. um TRY ocorre quando nenhuma excessão
# acontece, e o ELSE de um loop roda quando nenhum BREAK ocorre.

# o CONTINUE, por sua vez, continua para a próxima iteração do loop.

for num in range(2, 10):
    if num % 2 == 0:
        print("Encontrei um número par:", num)
        continue # o continue faz com que os numeros pares nao apareçam duas vezes.
    print("Encontrei um número:", num)

# 4.5 - PASS STATEMENTS:
# o pass não faz nada, pode ser utilizado quando for requerido algo sintatecamente
# mas o programa não requer ações.

# 4.6 - DEFINING FUNCTIONS 
# podemos criar uma função que escreva as séries de Fibonacci até um dado limite
# utilizamos DEF para criar uma função

def fib(n):
    """Escreve a sequência de Fibonacci até um número n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

fib(2000) # chamada da função
print()
# DEF introduz a definição de função, seguida por seu nome e os parâmetros, entre parenteses.
# depois disso, é definido o corpo da função, e deve estar identado.
# funções normalmente tem DOCSTRINGS, antes da definição do seu corpo.
# DOCSTRINGS são strings que documentam a função de alguma forma.
# os argumentos passados para a função são passados utilizando CHAMADAS POR VALOR, onde o 
# VALOR é SEMPRE uma REFERENCIA DO OBJETO, não o valor do objeto.
# a execução de uma função introduz uma nova symbol table utilizada para as variáveis da função.
# mais precisamente, todas as variaveis definidas nessa função, guardam seu valor nessa symble table local.
# quando uma função chama outra função, uma nova symbol table é definida para essa chamada.
# a definição da função introduz o nome dela na symbol table atual. o valor do nome da função possui um tipo
# que é reconhecido pelo interpretador como uma função definida pelo usuário, esse valor pode ser realocado
# em outro nome, que poderá ser usado como a função.

print(fib)
f = fib
f(100)

# ou seja, notamos que fib não é uma função em si, e sim um procedimento já que não retorna um valor.
# na verdade, mesmo funções sem um RETURN retornam um valor, que é NONE.
# podemos escrever uma função que armazene os números de fibonacci:

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)

# RETURN retorna o valor da função, que se torna NONE quando não há
# uma expressão ou quando a função chega direto até o fim.
# result.append chama um METÓDO do objeto lista RESULT. um metódo
# é uma função que 'pertence' a um objeto e é chamado obj.methodname
# no caso, o metodo append se equivale a result = result + [a], porém
# mais eficiente.