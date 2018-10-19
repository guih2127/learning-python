'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

print('digita ai o primeiro numero')
x = int(input())

print('digita seu segundo numero')
y = int(input())

print('digita o terceiro numero merda')
z = int(input())

print('produto do dobro primeiro com a metade do segundo: ' + str((x * 2) * (y // 2)))
print('soma do triplo do primeiro com o terceiro: ' + str((3 * x) + (z)))
print('terceiro elevado ao cubo: ' + str(z ** 3))