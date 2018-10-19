'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
 e informe-o expresso no formato horas:minutos:segundos.'''

x = int(input())

horas = x // (60 * 60)
minutos = (x - (horas * 60 * 60)) // 60
segundos = (x - (minutos * 60)) - (horas * 60 * 60) 

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))