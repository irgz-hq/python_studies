# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


# aqui eu defino a classe carro que recebe um motor e um fabricante
class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    def mostrar_motor(self):
        print(self.motor.nome)

    def mostrar_fabricante(self):
        print(self.fabricante.nome)

# aqui o motor 
class Motor:
    def __init__(self, nome):
        self.nome = nome

# aqui o fabricante
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fiat = Fabricante('Fiat')
v8 = Motor('V8')
uno = Carro('uno', motor=v8, fabricante=fiat)

print(uno.nome)
uno.mostrar_fabricante()
uno.mostrar_motor()