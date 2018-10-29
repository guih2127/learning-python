# o conceito de NESTED FUNCTIONS é a criação de funções dentro de uma outra função.

def f1():
	x = 8001
	def f2():
		print(x)
	f2()

f1()

# nested function que fornece um numero (x da função menor) elevado a outro (n da função maior):
def exp(n):
	def eleva(x):
		print(x**n)
	return eleva # aqui, retornamos, a partir da função EXP, a função ELEVA

# isso faz com que possamos atribuir a função EXP a uma variável, por exemplo, e
# então, chamar a função ELEVA a partir dessa variável, passando um parametro.

x = exp(3) # atribuimos a x a função exp, recebendo o n = 3

x(2) # como x = exp(3) e retorna ELEVA, passamos como parametro 2 para a própria função ELEVA.
x(3)
x(4)

# porem, inicialmente, nao podemos mudar variaveis de uma função de cima em uma nested function.
def f1():
	comeco = 0
	def f2():
		#comeco += 1 # isso irá retornar um erro, pois a variavel nao foi atribuida na função f2.
		nonlocal comeco
		comeco +=3
		print(comeco)
	return f2

x = f1()
x()

# ou seja, utilizamos NONLOCAL para conseguirmos chamar uma variável definida em outra função.
# o NONLOCAL é parecido com o GLOBAL, porém par NESTED FUNCIONS