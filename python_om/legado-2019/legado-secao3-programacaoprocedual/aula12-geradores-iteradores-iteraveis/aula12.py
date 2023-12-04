
lista = [0,1,2,3,4,5]

print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))

'''
A lista não é um iterador ou gerador, ela é iterável. O que o for faz é converter,
em tempo de execução, a lista em um iterador.

Gerador: ele gera os números e não os armazena
Lista: armazena todos os números na memória (custa mt mais memória)
'''

lista2 = iter(lista)

print(hasattr(lista2, '__iter__'))
print(hasattr(lista2, '__next__'))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))

import sys
import time

print(sys.getsizeof(lista), sys.getsizeof(lista2))

# como criar um gerador
print('###################################')

def gera():
    r = []
    for n in range(100):
        r.append(n)
       # time.sleep(0.1)
    return r

g = gera()

for v in g:
    print(v)

print('################')

def gerador():
    for n in range(100):
        yield n
        # time.sleep(0.1)

s = gerador()

for n in range(100):
    print(next(s))

# criando gerador da forma mais eficiente

gerador_def = (n for n in range(100))

print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))
print(next(gerador_def))

print('Olha o for pra completar')

for o in gerador_def:
    print(o)