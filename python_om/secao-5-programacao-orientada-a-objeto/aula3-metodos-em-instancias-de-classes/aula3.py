# Métodos em instâncias de classes Python

class Carro:

    def __init__(self, nome='Sei lá'):
        # self.nome = 'Fusca'  # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro('Celta')
print(celta.nome)

fusca.acelerar()
celta.acelerar()