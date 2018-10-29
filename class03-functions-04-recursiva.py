# inicialmente, não se pode referenciar uma função
# dentro de uma função.

def f(ops):
    #print(f()) <- isso retornará um erro
    f = ops
    print(f)

f(1)

# porém, existem funções RECURSIVAS, funções que referenciam
# à própria função.

# ex. função que retorna um numero fatorial:
def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat*=i
    return fat

print(fatorial(5))

# tratando a mesma função, com recursividade:
def fatorial_recursivo(num):
    if num==1: # se o numero for 1, apenas retornamos 1
        return num
    return fatorial_recursivo(num-1) * num # se nao for 1, chamamos a função dentro dela própria, ocasionando num loop

print(fatorial_recursivo(5))

# a recursividade não é muito citada em python, por não funcionar tão bem
# mas ainda assim, podem ser boas soluções de vez em quando.