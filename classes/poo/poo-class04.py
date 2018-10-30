# ABSTRAÇÃO, ATRIBUTOS/METÓDOS ESTÁTICOS E ENCAPSULAMENTO

# ABSTRAÇÃO:

class ObjetoGrafico(object):
    def __init__(self, cor):
        self.cor = cor
    
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def info(self):
        print('%f metros² serão preenchidos com a cor %s'(self.area(), self.cor()))

# aqui, criamos a classe OBJETO GRÁFICO, com alguns metódos, mas perceba que eles estão vazios.
# esse é o conceito de ABSTRAÇÃO, simplesmente não escrever nada, pois deixaremos as subclasses
# dessa classe preencherem esses metódos por nós.

# em POO, ABSTRAÇÃO é a HABILIDADE de concentrar nos aspectos essenciais de um contexto qualquer,
# ignorando características menos importantes. uma classe é uma ABSTRAÇÃO de entidades existentes.

# por exemplo, a abstração referente a classe animais possui várias sub-entidades, como répteis,
# mamíferos, etc, e cada uma dessas também possuem sub-classes, como humanos, jacarés, etc.

# uma classe abstrata é uma superclasse que não possui instâncias, ela define um modelo para
# uma funcionalidade e fornete uma implementação incompleta, que é compartilhada por um grupo
# de classes derivadas, cada uma delas completando a funcionalidade da classe abstrata.

# ATRIBUTOS/METÓDOS ESTÁTICOS:

class Cachorro:
    nome = 'Rex'
    cor = 'marrom'

dog = Cachorro()

print(dog.nome)
print(dog.cor)

# diferentemente do que possamos pensar, REX e MARROM são atributos da CLASSE CACHORRO,
# e não da instância DOG que criamos, ou seja, estes são considerados ATRIBUTOS ESTÁTICOS,
# pois poderemos acessá-los de qualquer instância que quisermos.

class Conta(object):
    total = 10000
    reserva = 0.1

    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        Conta.total += valor # fazendo isso, alteramos os VALORES ESTATICOS da classe CONTA.

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def imprime_reserva():
        print(Conta.total * Conta.reserva)

itau = Conta(123, 5000)
itau.deposito(1000)
itau.saque(5000)
print(itau.saldo)
print(Conta.total)

# podemos alterar os próprios valores estáticos da classe em si a partir de uma instância
# isso pode ser útil, por exemplo, se tivessemos várias contas, sempre modificando os metódos
# estáticos do banco em si através dos saques e depósitos.

Conta.deposito(itau, 4000)
print(itau.saldo)

# chamamos o metódo DEPÓSITO da classe CONTA, então, passamos ITAU e 4000 como argumentos,
# já que deposito recebe uma INSTÂNCIA de conta e um VALOR.
# isso é identico a chamarmos itau.deposito(4000), a diferença é que quando chamamos itau.deposito(4000)
# já estamos especificando a instância que queremos utilizar.

# itau.imprime_reserva() <- isso aqui irá retornar um ERRO, porque imprime_reserva NÃO RECEBE UMA INSTÂNCIA COMO
# ARGUMENTO (SELF), esse metódo só pode ser chamado através da classe, de tal forma:

Conta.imprime_reserva()

# ENCAPSULAMENTO:

# até agora, estivemos acessando valores com, por exemplo, Conta. e itau.
# porém, pode ser que não iremos querer que esses elementos sejam acessíveis por fora
# do objeto ou classe.
# por exemplo, não seria muito legal se conseguissem acessar a reserva do banco 
# através de uma conta em si.
# da mesma forma, nao seria muito bom se todos tivessem acesso ao id de uma conta.
# podemos esconder isso, de forma que tal objeto possa ser acessado somente em um lugar:

class Conta(object):
    __total = 10000
    __reserva = 0.1

    def __init__(self, id, saldo):
        self.__id = id
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += valor # fazendo isso, alteramos os VALORES ESTATICOS da classe CONTA.

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def imprime_reserva():
        print(Conta.__total * Conta.__reserva)

# para fazermos com que um elemento só possa ser chamado por sua própria instância, colocamos um
# __ antes dele, como fizemos com o id, total e reserva.

# print(Conta.__total, Conta.__reserva) <- quando definimos algo como private, não podemos acessá-lo assim.
# itau.id, itau.__id <- nem assim.

itau = Conta(123, 5000)

itau.deposito(300) # o depósito conseguimos fazer, pois nao colocamos como private.
itau.saque(1000) # o saque tambem.

Conta.imprime_reserva() # o imprime_reserva tambem funciona.

# a questão é que metodos e atributos PRIVATE só podem ser chamado DENTRO DA CLASSE,
# se tentarmos chama-los fora, receberemos um erro.
# o python só possui um tipo de encapsulamento, não é como no C# e no Java, onde existem mais
# tipos, o python só existe PUBLIC E PRIVATE, ou seja, ou ele pode ser acessado de qualquer lugar
# ou ele só pode ser acessado de dentro de uma classe.

# EXERCICIO:

# escreva um programa de bancos que possua:
# uma class Banco com os atributos: private total, public taxaReserva, private reservaExigida
# metodos private calculaReserva, public podeFazerEmprestimo = bool
# classe Conta com atributos private: id, senha, saldo e metodos: public deposito(senha, valor)
# public saque(senha, valor), public podeReceberEmprestimo(valor) -> bool, public saque (float)

class Banco(object):
    __total = 5000
    taxa_reserva = 0.1
    __reserva_exigida = 200

    def __init__(self):
        pass

    def __calcula_reserva():
        total_reserva = Banco.__total * Banco.total_reserva
        print('A reserva no momento é de %f.' %Banco.total_reserva)

    def pode_fazer_emprestimo():
        if (Conta.__total > 0):
            pode_emprestimo == True
        else:
            pode_emprestimo == False

    def aumenta_total(valor):
        valor = valor
        Banco.__total = Banco.__total + valor
        return Banco.__total

    def diminui_total(valor):
        valor = valor
        Banco.__total = Banco.__total - valor
        return Banco.__total

    def mostra_total():
        print('O total do banco é %s.' %Banco.__total)


class Conta(Banco):
    def __init__(self, id_num, senha, saldo):
        self.__id = id_num
        self.__senha = senha
        self.__saldo = saldo

    def deposito(self, senha, valor):
        senha = senha
        if senha == self.__senha:         
            valor = valor
            self.__saldo = self.__saldo + valor
            Banco.aumenta_total(valor)
            print('Deposito feito com sucesso.')
        else:
            print('Digite a senha correta.')
            return self.__saldo

    def saque(self, senha, valor):
        senha = senha
        if senha == self.__senha:
            valor = valor
            __saldo = self.__saldo - valor
            Banco.diminui_total(valor)
            print('Saque feito com sucesso.')
        else:
            print('Digite a senha correta.')
            return self.__saldo

    def ver_saldo(self, senha):
        senha = senha
        if senha == self.__senha:
            print('O seu saldo é %f.' %(self.__saldo))
        else:
            print('Digite a senha correta.')

bradesco = Conta(123, 123, 5000)

bradesco.deposito(12, 3000)

bradesco.deposito(123, 3000)

bradesco.ver_saldo(123)

Banco.mostra_total()














