from classes import *

"""
Associacao - Usa | Agregacao - Tem | Composicao - Eh dono | Heranca - É
"""

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 52)
print(a1.nome)
a1.falar()
a1.estudar()