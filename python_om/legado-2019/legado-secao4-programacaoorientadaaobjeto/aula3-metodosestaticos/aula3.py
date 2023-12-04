from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


    # aqui ele cria uma instancia pra gente, mesma coisa do __init__ so que em vez
    # de ser na escala de instancia eh na escala de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # staticmethod eh como se fosse uma funcao normal, que nao precisa da instancia
    # e nem da classe, mas por questao de organizacao, fica dentro da classe
    @staticmethod
    def gera_id():
        rand = randint(10000, 99999)
        return rand


#p1 = Pessoa('Luigui', 26)
p1 = Pessoa.por_ano_nascimento('Luigui', 1996)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# chamando pela classe
print(Pessoa.gera_id())

# chamando pela instancia
print(p1.gera_id())