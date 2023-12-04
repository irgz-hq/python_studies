"""
Combinations, permutations, product - itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Luigui', 'João', 'Larissa', 'Joilza', 'Ivanildo']

print('A ordem não importa')
for grupo in combinations(pessoas,2):
    print(grupo)

print()
print('A ordem importa')
for grupo in permutations(pessoas,2):
    print(grupo)

print()
print('A ordem importa e pode repetir')
for grupo in product(pessoas,repeat=2):
    print(grupo)