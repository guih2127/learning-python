a, b = (input().split(" "))
a, b = int(a), int(b)

if (a == b):
    print('O JOGO DUROU 24 HORA(S)')

if (a < b):
    print('O JOGO DUROU ' + str(b - a) + ' HORA(S)')

if (a > b):
    print('O JOGO DUROU ' + str(abs(24 - a) + b) + ' HORA(S)')