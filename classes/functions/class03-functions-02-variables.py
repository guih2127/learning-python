# supondo que temos a função:

def incrementa(x):
    x += 1

y = 10
incrementa(y)
print(y)

# o valor não muda, por que?
# quando chamamos uma função, no caso, passando a variável y
# como argumento, o python cria uma CÓPIA da variável e a utiliza
# na função.

def incrementa(x):
    x+= 1
    print(x)

# nesse caso, o valor realmente foi incrementado, por que?
# DENTRO da função, a cópia foi feita, incrementada em 1,
# e então o imprimiu com a função print, porém, a variável y
# continuou intocada.
# se tentarmos utilizar a variável x, definida na função incrementa,
# receberemos um erro, pois ela é uma variável LOCAL.

def incrementa(x):
    incremento = 5 # variável local
    x += incremento # cópia do valor
    print(x)

# podemos chamar variáveis GLOBAIS dentro de funções, de tal forma:

def incrementa():
    global X # obtemos a variável global X e trabalhamos com ela 
    incremento = 5
    X += incremento

# função utilizando funções globais, é uma boa pratica criar
# uma função MAIN, que será o programa em si.
contas = []
depositos = []
saldo = 0

def main():
    opcao = bool(int(input("Deseja criar conta? (1) SIM (0) FECHAR")))
    while opcao:
        cria_conta()
        ver_saldo()
        opcao = bool(int(input("Deseja continuar utilizando o programa? (1) SIM (0) FECHAR")))    

def cria_conta():
    global contas, depositos, saldo
    num_conta = int(input("Digite um número de conta: "))

    while num_conta in contas:
        num_conta = int(input("Número ja existente, digite um número de conta: "))

    contas.append(num_conta)

    deposito = float(input("Digite o valor do seu depósito: "))
    while deposito <= 0:
        deposito = float(input("Digite um valor real para seu depósito: "))
    
    depositos.append(deposito)
    saldo += deposito

def ver_saldo():
    global saldo
    opcao = bool(int(input("Deseja ver o seu saldo no banco? 1 para sim e 0 para não.")))
    if opcao:
        print('O saldo do banco é R$', saldo)

main()