# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# obtem o valor do atributo cor
# cor -> get_cor()

# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯 (não chama ela com parenteses)
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # aqui a property ta fazendo com que o metodo se comporte como atributo
    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_corpo(self):
        return 'Transparente'
######################
# código cliente

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_corpo)


##################################
# aqui eh o primeiro exemplo de getter

"""
class Caneta:
    def __init__(self, cor):
        # em outras linguagens a gente tem private, protected, public, eh ai que
        # se constroi a lógica do getter
        self.cor_tinta = cor

    # isso aqui eh um getter
    def get_cor(self):
        print('GET COR')
        return self.cor_tinta
"""