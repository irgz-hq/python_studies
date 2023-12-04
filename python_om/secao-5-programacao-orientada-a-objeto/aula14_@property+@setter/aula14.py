# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):

        # aqui eh uma conveção, atributo interno da classe "olha desenvolvedor
        # nao utilize esse atributo"
        # private, protected (isso aqui eh privado, eh meu), public (normal)
        # lembrando se eu settar o valor com o mesmo nome do setter, ele vai passar no setter
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    # nao eh boa pratica se ter dois metodos de mesmo nome, mas podemos chamar
    # um setter, que seria o nome da property (nesse caso "cor") seguido de
    # .setter

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

    def printando_atributor_init(self):
        print(self.cor)
        print(self._cor_tampa)

caneta = Caneta('Azul')
# aqui o codigo executa normalmente, mesmo tendo alterado o atributo .cor
# entao, basicamente o property serve para pegar o valor e o setter para
# settar um outro valor caso o usuário queira

caneta.cor = 'Vermelho'
print(caneta.cor)
print(caneta._cor)

caneta.cor_tampa = 'Azul'
print(caneta.cor_tampa)

caneta.printando_atributor_init()


# pelo o que eu entendi, basicamente o getter e o setter serve para pegar o valor
# e settar, respectivamente, sem precisar mexer no self._alguma coisa, para nao quebrar
# o código, o getter serve pra fazer um metodo se comportar como atributo como a gente viu
# ja o setter serve para atribuir um valor fora da classe.