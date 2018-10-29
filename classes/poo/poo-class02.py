# OBJETOS E CLASSES X DICIONÁRIOS:

# criando um novo dicionário da pessoa Lucas.
Pessoa = {'Nome': 'Lucas', 'Emprego': 'Advogado', 'Idade': 20, 'Cor de Cabelo': 'Preto'} 

# alterando o nome da pessoa.
Pessoa['Nome'] = 'João'

# adicionando um novo campo no dicionário pessoa.
Pessoa['Peso'] = 75

print(Pessoa)

class Pessoa:
	pass # o pass é simplesmente para criar uma classe vazia, dentre outras coisas.

Lucas = Pessoa()

Lucas.nome = 'Lucas'
Lucas.emprego = 'Advogado'
Lucas.idade = 20
Lucas.cor_de_cabelo = 'Preto' # se pararmos para prestar atenção, veremos que uma classe
# se comporta de maneira semelhante a um dicionário, e não é pra menos, podemos fazer:

print(Lucas.__dict__) # para chamar todos os atributos de um objeto em forma de dicionário.

# os OBJETOS são melhores por alguns motivos para se utilizar nestes casos, pois é mais fácil
# de criar diversos objetos, com metódos diferentes, do que dicionários. Além disso, com objetos,
# podemos utilizar de herança, polimorfismo, dentre outras técnicas, fazendo com que seja melhor
# trabalhar com os objetos e classes do que em dicionários.
# é importante saber disso, pois o fato dos objetos estarem armazenados em dicionários, no python,
# faz com que a linguagem se torne mais lenta.

# para uma classe um pouco mais complexa, como:

class Pessoa:
	def __init__(self, nome, emprego, idade):
		self.nome = nome
		self.emprego = emprego
		self.idade = idade

	def ola(self):
		print('Olá, meu nome é %s e eu tenho %f anos' %(self.nome, self.idade))

Lucas = Pessoa('Lucas', 'Advogado', 20)

print(Pessoa.__dict__) # vemos que uma classe possui mais itens em seu dicionário.
# isso acontece porque o dicionário de uma classe mostra também seus metódos,
# o que pode ser muito útil em várias situações.

