# HERANÇA E POLIMORFISMO:

class Mamifero:
	def __init__(self, cor_de_pelo, genero, num_de_patas):
		self.cor_de_pel = cor_de_pelo
		self.genero = genero
		self.num_de_patas = num_de_patas

	def falar(self):
		print('Olá, sou um mamífero e eu sei falar!')

	def andar(self):
		print('Estou andando sobre %i patas' %(self.num_de_patas))

	def amamentar(self):
		if self.genero.lower()[0] == 'm':
			print('Machos não amamentam.')
			return
		print('Amamentando meu filhote.')

Rex = Mamifero('marrom', 'masculino', 4) 

Rex.falar()
Rex.amamentar()
Rex.andar() # nesse caso, os metodos da classe fizeram sentido, já que Rex é um animal.

Julia = Mamifero('preta', 'feminino', 2)

Julia.andar()
Julia.amamentar()
Julia.falar() # nesse caso, os metodos nao fizeram muito sentido, já que Júlia, mesmo
# sendo um mamífero, é um ser humano.

# por isso, algumas vezes, podemos querer criar classes dentro de classes.
# ou seja, podemos querer criar SUBCLASSES que HERDEM caracteristicas de SUPERCLASSES.
# esse conceito é conhecido como HERANÇA.

class Pessoa(Mamifero): # aqui, ja identificamos que Pessoa é uma SUBCLASSE da classe MAMÍFERO.
	pass

Julia = Pessoa('preta', 'feminino', 2)

Julia.andar()
Julia.amamentar()
Julia.falar() # ou seja, conseguimos acessar os metodos e atributos da SUPERCLASSE (mamífero).

# o conceito de HERANÇA, em POO, se refere as classes e sua HIERARQUIA.

# mas podemos fazer mais do que isso.

class Pessoa(Mamifero):
	def __init__(self):
		self.cabelo = 'loiro' # com o que fizemos agora, REESCREVEMOS O METODO INIT DA SUPER CLASSE, 
# pois como ambas tem o mesmo nome, o metódo foi reescrito, e agora pessoa nao precisa mais de receber atributos. 

Julia = Pessoa() 

# Julia.amamentar() # ao tentarmos fazer isso, receberemos um erro, pois as variáveis do metódo construtor de Mamifero não existirão mais,
# já que o metódo construtor foi reescrito na subclasse.

# porém, podemos chamar o metódo construtor de MAMÍFERO dentro da subclasse PESSOA:

class Pessoa(Mamifero):
	def __init__(self, cor_de_pelo, genero, andar, cabelo):
		super(Pessoa, self).__init__(cor_de_pelo, genero, andar) # para fazer isso, utilizamos o SUPER, e passamos pra ele
		# o nome da classe e a própria instância do objeto, self, então, colocamos .nome do metódo, que no caso é o __init__, e passamos
		# os atributos necessários para ele.
		self.cabelo = cabelo
		self.cor_de_pelo = cor_de_pelo

Julia = Pessoa('preta', 'feminino', 2, 'loiro')

# e agora podemos usar os outros metódos da SUPERCLASSE Mamífero.

print(Julia.cor_de_pelo)
Julia.andar()
Julia.amamentar()
Julia.falar()

# isso remete ao conceito de POLIMORFISMO, caracterizado quando duas ou mais classes possuem METÓDOS DE MESMO NOME, 
# e podemos utilizar QUALQUER UM DELES sem trata-los de forma diferenciada.
# ou seja, POLIMORFISMO se refere a VARIAS FORMAS DE CHAMAR UM METÓDO. quem decide a forma com que o metodo sera chamado
# é o objeto chamado.

# então, o SUPER serve para que a SUBCLASSE se refira explicitamente a SUPERCLASSE.
# é uma boa prática que todas as classes criadas sejam subclasses da classes OBJECT do python:

class Animal(object):
	pass








