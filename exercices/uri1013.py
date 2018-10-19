'''Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.'''

a, b, c = (input().split(" "))
a, b, c = int(a), int(b), int(c)

if (a > b and a > c):
        print(str(a) + ' eh o maior')
elif (b > a and b > c):
        print(str(b) + ' eh o maior')
elif (c > a and c > b):
        print(str(c) + ' eh o maior')

