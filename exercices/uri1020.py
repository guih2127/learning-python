'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e 
informe-a em anos, meses e dias
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias 
e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.'''

x = int(input())

anos = x // 365
resto_dias = x - (anos * 365)
meses = resto_dias // 30
resto_dias = x - (anos * 365) - (meses * 30)
dias = resto_dias

print(str(anos) + " ano(s)")
print(str(meses) + " mes(es)")
print(str(dias) + " dia(s)")
