a, b, c = (input().split(" "))

a, b, c = float(a), float(b), float(c)

numeros = [a, b, c]

numeros = sorted(numeros, reverse=True)

a = numeros[0]
b = numeros[1]
c = numeros[2]


if a >= (b + c):
    print('NAO FORMA TRIANGULO')

else:
    if a**2 == (b**2 + c**2):
        print('TRIANGULO RETANGULO')

    if a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')

    if (b**2 + c**2) > a**2:
        print('TRIANGULO ACUTANGULO')

    if a == b and b == c:
        print('TRIANGULO EQUILATERO')

    if (a == b and a != c) or (b == c and c != a) or (c == a and c != b):
        print('TRIANGULO ISOSCELES')
