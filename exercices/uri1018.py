'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
 As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.'''

x = int(input())

print(x)
divisao_por_cem = x // 100
print(str(divisao_por_cem) + ' nota(s) de R$ 100,00')
x = x - (divisao_por_cem * 100)
divisao_por_cinquenta = x // 50
print(str(divisao_por_cinquenta) + ' nota(s) de R$ 50,00')
x = x - (divisao_por_cinquenta * 50)
divisao_por_vintecinco = x // 20
print(str(divisao_por_vintecinco) + ' nota(s) de R$ 20,00')
x = x - (divisao_por_vintecinco * 20)
divisao_por_dez = x // 10
print(str(divisao_por_dez) + ' nota(s) de R$ 10,00')
x = x - (divisao_por_dez * 10)
divisao_por_cinco = x // 5
print(str(divisao_por_cinco) + ' nota(s) de R$ 5,00')
x = x - (divisao_por_cinco * 5)
divisao_por_dois = x // 2
print(str(divisao_por_dois) + ' nota(s) de R$ 2,00')
x = x - (divisao_por_dois * 2)
divisao_por_um = x // 1
print(str(divisao_por_um) + ' nota(s) de R$ 1,00')



    


