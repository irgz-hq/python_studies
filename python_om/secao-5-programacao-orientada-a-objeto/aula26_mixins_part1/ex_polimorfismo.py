class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

def fazer_som_do_animal(animal):
    return animal.fazer_som()

# Uso de polimorfismo
cachorro = Cachorro()
gato = Gato()

print(fazer_som_do_animal(cachorro))  # Resultado: Au Au
print(fazer_som_do_animal(gato))      # Resultado: Miau
