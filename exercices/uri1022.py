numero_casos = int(input())
saida = []

def mmc(x, y):
    divisores_x = []
    divisores_y = []
    divisores_comum = []
    for i in range(1, (abs(x) + 1)):
        if x % i == 0:
            divisores_x.append(i)

    for i in range(1, (abs(y) + 1)):
        if y % i == 0:
            divisores_y.append(i)

    for divisor_x in divisores_x:
        for divisor_y in divisores_y:
            if divisor_x == divisor_y:
                divisores_comum.append(divisor_x)

    x = max(divisores_comum)
    return int(x)

for i in range(0, numero_casos):
    n1, div1, d1, operacao, n2, div1, d2 = (input().split(" "))
    n1, div1, d1, operacao, n2, div1, d2 = int(n1), str(div1), int(d1), str(operacao), int(n2), str(div1), int(d2)

    if operacao == '+':
        n = (n1 * d2 + n2 * d1)
        d = (d1 * d2)
        x = mmc(n, d)
        n2 = int(n / x)
        d2 = int(d / x)
        saida.append(str(n) + '/' + str(d) + ' = ' + str(n2) + '/' + str(d2))
    
    elif operacao == '-':
        n = (n1 * d2 - n2 * d1)
        d = (d1 * d2)
        x = mmc(n, d)
        n2 = int(n / x)
        d2 = int(d / x)
        saida.append(str(n) + '/' + str(d) + ' = ' + str(n2) + '/' + str(d2))

    elif operacao == '*':
        n = (n1 * n2)
        d = (d1 * d2)
        x = mmc(n, d)
        n2 = int(n / x)
        d2 = int(d / x)
        saida.append(str(n) + '/' + str(d) + ' = ' + str(n2) + '/' + str(d2))

    elif operacao == '/':
        n = (n1 * d2)
        d = (n2 * d1)
        x = mmc(n, d)
        n2 = int(n / x)
        d2 = int(d / x)
        saida.append(str(n) + '/' + str(d) + ' = ' + str(n2) + '/' + str(d2))

for x in saida:
    print(x)




