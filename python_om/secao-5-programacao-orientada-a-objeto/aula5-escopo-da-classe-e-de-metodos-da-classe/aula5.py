# Escopo da classe e de métodos da classe
class Animal:
    #  nome = 'Leão'

    def __init__(self, nome):
        # aqui ta no escopo da instancia da classe
        # escopo do self pode ser acessado por qualquer metodo na classe
        self.nome = nome

        # aqui ta no escopo do init
        variavel = 'valor'
        print(variavel)

    def comendo(self, *alimento):
        return f'{self.nome} esta comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã', 'abóbora'))
