# o python já possui uma série de classes implementadas, tais como
# listas, tuplas, etc.
# mas e para criar um objeto?

class MeuObjeto:
	def __init__(self, n, i): # essa é a sintaxe para criação do METÓDO CONSTRUTOR. 
		self.nome = n # quando utilizamos SELF, nos referimos ao OBJETO da classe.
		self.idade = i				# então, podemos dizer que o objeto da classe MeuObjeto terá um atributo NOME.
		print('Construtor chamado com sucesso.')

	def imprime(self): # sempre que formos criar METÓDOS de classes, teremos de REFERENCIAR o objeto, com SELF.
		print('Olá, meu nome é %s e eu tenho %d anos.'%(self.nome, self.idade))

Guilherme = MeuObjeto('Guilherme', 24) # Estamos criando um OBJETO chamado Guilherme, ATRAVÉS da CLASSE MeuObjeto
Guilherme.imprime()


# ATRIBUTOS:

class Minha:
	def __init__(self):
		self.x = 0
		self.y = 0 # criamos uma classe basica, com x e y

meu = Minha() # criamos uma instancia da classe Minha, com o nome meu
print(meu.x, meu.y) #chamamos as variáveis x e y dentro da instancia meu, utilizando meu.x e meu.y

meu.x = 5 # podemos tambem trocar o valor de x, mesmo fora da classe
print(meu.x)

meu.z = 10 # podemos criar novos atributos para o objeto, mesmo fora da classe
print(meu.z)

# ASSOCIAÇÕES:

class Pessoa: # criamos uma classe pessoa.
	def __init__(self, nome, peso, cao): # o metodo construtor recebe por parametro self, nome, peso e cao.
		self.nome = nome # as variaveis nome, peso e cao serao os valores de mesmo nome passados por atributo.
		self.peso = peso
		self.cao = cao

	def treinar(self): # criamos um metodo treinar, que possui dois metodos da classe cachorro dentro dele.
		self.cao.da_a_patinha()
		self.cao.latir()

class Cachorro: # criamos a classe cachorro.
	def __init__(self, nome, cor): # o metodo construtor recebe por parametro self, nome e cor.
		self.nome = nome # as variaveis nome e cor serao os valores de mesmo nome passados por atributo
		self.cor = cor

	def da_a_patinha(self):
		print('%s extendeu a patinha' %self.nome)

	def latir(self):
		print('AUAUAUAUAUAUAUAU')

rex = Cachorro('Rex', 'marrom') # criamos uma instancia da classe Cachorro, chamado Rex.

Guilherme = Pessoa('Guilherme', 80, rex) # criamos uma instancia do objeto Pessoa, chamado Guilherme, que recebe por atributo
# seu nome, peso e a instancia Rex que criamos a partir do objeto Cachorro.

print(Guilherme.nome, Guilherme.peso, Guilherme.cao.nome, Guilherme.cao.cor) # Podemos acessar os atributos do objeto REX através do objeto GUILHERME.
Guilherme.treinar() # podemos chamar o metodo treinar do objeto Guilherme, que então irá chamar os dois metodos do objeto cachorro.

# FUNÇÕES:

print(Guilherme.nome)

def MudaNome(pessoa):
	pessoa.nome = 'Lucas'

MudaNome(Guilherme)
print(Guilherme.nome) # podemos ver que, ao mudarmos um atributo do objeto mesmo fora dele, o atributo é trocado normalmente, como acontece com listas, etc.


