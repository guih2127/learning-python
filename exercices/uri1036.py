'''Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". 
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, 
com uma mensagem correspondente conforme exemplo abaixo. 
Imprima sempre o final de linha após cada mensagem.'''

a, b, c = (input().split(" "))
a, b, c = float(a), float(b), float(c)

# 10.0 20.1 5.1

if (a <= 0):
    print("Impossivel calcular")

else:
    delta = ((b**2) - 4 * a * c)**0.5
    delta1 = str(delta)

    if ('j' in delta1):
        print("Impossivel calcular")

    else:
        r1 = (-b + delta) / (2 * a)
        r2 = (-b - delta) / (2 * a)

        r1 = format(r1, '.5f')
        r2 = format(r2, '.5f')

        print("R1 = " + str(r1))
        print("R2 = " + str(r2))