# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

# azulzinhos sao classes

# herdando tudo de string
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        # super eh capaz de chamar o metodo da calsse acima
        return super().upper()

string = MinhaString('Luiz')
print(string.upper())

print('###################')
print()

class A:
    atributo_a = 'valor_a'

    def metodo(self):
        print('A')

class B:
    atributo_b = 'valor_b'

    def metodo(self):
        print('B')

class C:
    atributo_c = 'valor_c'

    def metodo(self):
        # aqui eu to sendo explicito
        super(C, self).metodo()
        print('C')