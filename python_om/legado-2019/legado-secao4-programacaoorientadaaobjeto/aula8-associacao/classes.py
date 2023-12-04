class Escritor:

    # construtor ta fazendo o papel de setter nesse caso
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    # como criamos um atributo privado, nao conseguimos acessa-lo fora da classe
    # entao precisamos criar pelo menos um getter para fazer isso!

    # lembrando que a funcao definida abaixo do getter, se comporta agora como um
    # atributo, entao pra chamalo, temos que digitar a instancia.nome

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')
class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')