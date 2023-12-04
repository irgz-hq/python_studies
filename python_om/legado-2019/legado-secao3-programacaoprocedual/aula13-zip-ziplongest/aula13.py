"""
Zip - Unindo iteráveis
Zip longest - Itertools (precisa importar) (pode ser com itertools)
"""

# Não usar zip longest com count, pq o count é um gerador e geradores são infinitos

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']
cidades_estados = zip(cidades, estados)
cidades_estados_2 = zip(cidades, estados)
cidade_estados_3 = zip_longest(indice, cidades, estados,
                               fillvalue='Estado')
print(type(cidades_estados))

print(list(cidades_estados))
print('zip_longest', list(cidade_estados_3))
print(dict(cidades_estados))

# ver essa questão de dicionário da lista
print(dict(cidades_estados_2))
print(dict(estados))