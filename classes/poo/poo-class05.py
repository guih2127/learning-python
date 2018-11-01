# METÓDOS E ATRIBUTOS ESPECIAIS:

# alguns metodos especiais, nos ja vimos, como o __init__
# existem diversos metodos que cumprem diversos papeis,
# o metodo dict por ex. retorna um dicionario, e o init constroi a instancia.

class Conta:
  """
  Objeto do tipo Conta, representa uma conta num banco qualquer
  """
  def __init__(self, ID, saldo):
    """
    Construtor da classe Conta
    """
    self.ID = ID
    self.saldo = saldo
  
  def __str__(self):
    """
    Devolve uma string representando a conta
    """
    return 'ID: %i\nSaldo: R$ %.2f'%(self.ID, self.saldo)
  
  def __add__(self, other):
    """
    Permite somar uma conta com outra
    """
    self.saldo += other.saldo

bradesco = Conta(456, 5000)
print(bradesco)
print(bradesco.__dict__) # retorna um dicionario do objeto

itau = Conta(123, 4000)
print(itau)

itau + bradesco

print(bradesco)
print(itau)

# ou seja, vemos que o metodo __str__ serve para converter
# o objeto em uma string. o __str__ deve sempre retornar uma string.

# o metodo add serve para definirmos o que será feito quando
# somarmos uma instancia com outra instancia, no caso, 
# definimos que ao somarmos duas instancias, a primeira
# receberá o saldo da segunda.
# porem existem algumas limitações, no caso por exemplo,
# nao conseguiriamos somar mais de dois valores, a nao ser que
# colocassemos um * antes do argumento, especificando que o numero
# de argumentos não será especifico.

# também possuimos os metódos __sub__, __div__ e __mult__, que equivalem
# respectivamente a subtração, divisão e multiplicação de um objeto por outro.

# o __doc__ nos mostra a documentação de uma classe, objeto, metodo ou etc.
print(bradesco.__doc__)
print(bradesco.__init__.__doc__) 

# com o help, conseguimos passar por todos os metodos dentro de uma classe ou objeto, por ex:
# help(bradesco)

print(bradesco)

class Pai:
  pass

class Filha(Pai):
  pass

class Neta(Filha):
  pass

print(issubclass(Pai, Filha))
print(issubclass(Filha, Pai))

# o metodo is sub class serve para sabermos se uma classe é subclasse de outra.

print(Filha.__bases__) # tambem conseguimos ver a superclasse de uma subclasse assim.
# porem, o bases retorna so a superclasse DIRETA da subclasse, ou seja, um nivel acima.

print(callable(Pai)) # com callable, podemos descobrir se uma classe é instanciavel ou não.
# print(callable(5)) # retorna false

# por padrao, uma instancia nao é callable, se quisermos que uma instancia possa ser chamada,
# por ex. bradesco(), precisamos definir um metodo __call__