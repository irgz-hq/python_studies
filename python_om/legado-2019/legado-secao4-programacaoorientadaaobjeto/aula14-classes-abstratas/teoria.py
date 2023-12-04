"""
Classes abstratas sao classes que nao "querem" ser instanciadas

Classes abstratas podem ter métodos concretos e métodos abstratos

métodos abstratos é um método que não tem corpo, ou seja, as classes filhas que
usarem esse método, vai construir ele

métodos concretos são métodos que tem corpo, ou seja, já são bem definidos
"""
# abc = abstract base method

from abc import ABC, abstractmethod

# para a classe A ser uma classe abstrata tem que ter um metodo abstrato
class A(ABC):
    @abstractmethod
    def falar(self):
        pass

# a classe B só pode ser instanciada se tiver o método falar, já q ela herdou da classe A

"""
exemplo: classe abstrata Pessoa, classe Cliente e classe Estudante vai herder alguns metodos
abstratos da classe Pessoa, mas você não tem interesse em instanciar Pessoa, então as outras
classes herdam os métodos abstratos de Pessoa e elas estão responsáveis por defini-los agora.
"""
class B(A):
    def falar(self):
        print("falando...")

a = B()
a.falar()

