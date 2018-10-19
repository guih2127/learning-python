'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. '''

a, b, c = (input().split(" "))

a, b, c = float(a), float(b), float(c)

triangulo = format(((a * c) / 2), '.3f')
circulo = format(((3.14159) * (c ** 2)), '.3f')
trapezio = format((((a + b) / 2) * c), '.3f')
quadrado = format((b * b), '.3f')
retangulo = format((a * b), '.3f')

print('TRIANGULO: ' + str(triangulo))
print('CIRCULO: ' + str(circulo))
print('TRAPEZIO: ' + str(trapezio))
print('QUADRADO: ' + str(quadrado))
print('RETANGULO: ' + str(retangulo))
