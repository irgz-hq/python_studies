class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')

# aqui eu to falando que a classe Cliente tambem eh uma pessoa, ou seja
# herda todas as caracteristicas de Pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print(f'Estou em cliente')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')

"""
class ClienteVIP(Cliente):
    def falar(self):

        # essa funcao super() vai chamar o metodo falar() da classe hierarquicamente acima e
        # depois vai executar o metodo definido dentro da classe atual normalmente
        super().falar()
        print(f'{self.nomeclasse} está falando algo importante...')
"""

class ClienteVIP(Cliente):

    # aqui estamos definindo um inicializador a partir do init da classe Pessoa, note
    # que esse novo inicializador pede o sobrenome enquanto em Pessoa não pede, então
    # é só adicionar normalmente.
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self,nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        # lembrando que quando voce especifica o metodo que vc quer puxar, vc tem q enviar
        # o argumento necessario, ex: se for self é self!
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome}{self.sobrenome}')