# SETTER = CONFIGURANDO UM VALOR (=) (TEMOS QUE TER UM GETTER)
# GETTER (PODEMOS TER GETTER SOZINHO) = OBTER UM VALOR (.)
# GETTER E SETTER QUANDO USADO JUNTOS, TEM O MESMO NOME E O MESMO RETORNO
class Pessoa:
    def __init__(self, nome):

        # definindo self.nomedosetter = nome, voce chama o setter e esse atributo vai
        # ser configurado la no setter
        self.nome = nome


    # a property indica que vamos ter a funcao abaixo dela como um atributo, e nao
    # mas como um metodo.
    @property
    def nome(self):
        return self.qualquernomedesdequesejaigualaosetteregetter

    # para criar um setter, eu tenho que pegar um metodo que usei @property para decoralo
    # e em seguida colocar @{nome}.setter, segue o exemplo abaixo
    # a funcao do setter vai ser definida da mesma maneira que o getter, com uma diferenca
    # ela vai receber um valor para ser configurado
    @nome.setter
    def nome(self, valor): #o nome do valor, pode ser qualquer nome
        print("O setter foi executado")
        valor += 'Sobrenome'
        self.qualquernomedesdequesejaigualaosetteregetter = valor

    # um getter independente do setter, so pra retornar um valor
    @property
    def sobrenome(self):
        return 'Qualquer Sobrenome'

# uma vez configurado no setter, quando eu chamar (self.nome = qqcoisa) ou (p1.nome = qqcoisa) tá caindo no setter,
# e o que vier depois do simbolo de =, vai ser o valor configurado pelo setter.

"""
Atencao: instancia.nome = 'qualquer coisa', estou chamando o setter
         instancia.nome estou usando o getter
"""

p1 = Pessoa('Luluska')
print(p1.nome)
print(p1.sobrenome)



print("####################################")
# chamando o setter
p1.nome = "Luigui"
print(p1.qualquernomedesdequesejaigualaosetteregetter)

# chamando o getter
print(p1.nome)
print(p1.qualquernomedesdequesejaigualaosetteregetter)