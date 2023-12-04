# Encapsulamento (modificadores de acesso: public, protected, private)
# 4 pilares, encapsulamento, abstração, herença e polimorfismo
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é public'
        self._protected = 'isso é protected'
        self.__private = 'isso é private'

    def metodo_publico(self):

        # nao consigo acessar isso fora da classe
        print(f.__private)
        print(f.__metodo_privado())
        return 'metodo_publico'
    
    def _metodo_protegido(self):
        return '_metodo_protegido'
    
    def __metodo_privado(self):
        return '__metodo_privado'

f = Foo()
print(f.public)
print(f.metodo_publico())

# nao eh pra estar aqui
print(f._protected)
print(f._metodo_protegido())

# isso tbem nao eh pra ta aqui
print(f._Foo__metodo_privado())