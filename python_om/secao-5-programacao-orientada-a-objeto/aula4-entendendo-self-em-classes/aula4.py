# Métodos em instâncias de classes Python
# Classe - Molde (geralmente sem dados)
# Instancia de class (objeto) - Tem os dados
# Uma classe pode gerar várias instancias.
# Na classe o self eh a prorpia instancia
class Carro:

    def __init__(self, nome='Sei lá'):
        # self.nome = 'Fusca'  # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')

# eu preciso passar a instancia para o self nesse caso
Carro.acelerar(fusca)
print(fusca.nome)

celta = Carro('Celta')
print(celta.nome)

fusca.acelerar()
celta.acelerar()