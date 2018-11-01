# COMPARAÇÕES E EXTENDENDO OBJETOS DO PYTHON

class Conta:
	def __init__(self, i, s):
		self.ID = i
		self.saldo = s

	def deposito(self, v):
		self.saldo += v

	def saque(self, v):
		if self.saldo >= v:
			self.saldo -= v

	def __le__(self, outro):
		if self.ID <= outro.id:
			return True
		return False

	def __eq__(self, outro):
		if self.ID == outro.ID:
			return True
		return False

	def __ge__(self, outro):
		if self.ID >= outro.ID:
			return True
		return False

itau = Conta(123, 4000)
bradesco = Conta(123, 5000)

print(itau == bradesco) ## false, sera que é por que eles tem atributos diferentes?

bradesco2 = Conta(123, 4000) # false, ou seja, por que ele nos retorna false?

# quando perguntamos se dois objetos sao iguais, perguntamos na verdade se 
# duas variaveis APONTAM PRO MESMO OBJETO

itau3 = itau
itau3.deposito(500)

print(itau.saldo) # o saldo do itau foi mudado, mas por que? porque assim ambos
# itau3 e itau olham para o mesmo objeto, ja que a variavel armazena o endereço
# de memoria do objeto, e nao o objeto em si

print(itau3 == itau)  # retorna true!

print(id(itau))
print(id(itau3))

# a função id nos mostra o endereço de memoria no qual a nossa variavel esta armazenada

# porem, temos alguns metodos que nos permitem mudar os modos como são feitos
# as comparações em python, sendo eles:

# __le__ x <= y,
# __eq__ x == y,
# __ge__ x >= y,
# __lt__ x < y,
# __gt__ x > y,
# __ne__ x != y,

# esses metodos devolvem um metodo bool true ou false, e nos permite fazer
# comparações customizaveis

print(itau == bradesco)
