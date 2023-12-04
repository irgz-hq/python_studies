# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy
from dados.produtos import produtos

# Para aumentar os produtos em 10%, ja que estou usando dicionario
# vou utilizar list comprehension

# fazer uma deep copy

novos_produtos = copy.deepcopy(produtos)

# muita atencao aqui, os dois ** serve para desempacotar ou empacotar itens de dicionarios
# entao usei para desempacotar em um dicionario e criei uma nova chave preco obdecendo a
# devida transformação que preciso e ele substitui a chave antiga de mesmo nome

novos_produtos = [{**p, 'preco': round(p['preco']*1.1, 2)} for p in produtos]
print(*novos_produtos, sep='\n')
print('##########################')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# para ordenar vamos utilizar a função sort, mas precisamos passar uma funcao para ela
# a funcao deve receber o item do dicionario e retornar a chave da qual ela deve ser ordenada

"""
Aqui é como seria feito sem funcao lambda

def ordena_nome(item):
    return item['nome']


novos_produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

novos_produtos_ordenados_por_nome = sorted(novos_produtos, key=ordena_nome, reverse=True)
print(*novos_produtos_ordenados_por_nome, sep='\n')

"""
# com funcao lambda

novos_produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

novos_produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda p: p['nome'], reverse=True)
print(*novos_produtos_ordenados_por_nome, sep='\n')
print('#################')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

novos_produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda p: p['preco'])
print(*novos_produtos_ordenados_por_nome, sep='\n')
