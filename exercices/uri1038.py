'''Com base na tabela abaixo, escreva um programa que leia o código de um item e 
a quantidade deste item. 
A seguir, calcule e mostre o valor da conta a pagar.'''

codigo, quantidade = (input().split(" "))
codigo, quantidade = int(codigo), int(quantidade)

if (codigo == 1):
    preco = 4.00
elif (codigo == 2):
    preco = 4.50
elif (codigo == 3):
    preco = 5.00
elif (codigo == 4):
    preco = 2.00
elif (codigo == 5):
    preco = 1.50

precoTotal = quantidade * preco

print("Total: R$ " + str(precoTotal) + "0")