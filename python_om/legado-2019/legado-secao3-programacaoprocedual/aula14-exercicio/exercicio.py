"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados do
tamando da menor lista.

Exemplo:
lista_a = [1, 2, 3, 4]
lista_b = [1, 3, 5, 6, 7]

lista_soma = [2, 5, 8, 10]
"""

# listas
lista_a = [2, 5, 8, -3, -5, -2, -30, -5, 20, 90]
lista_b = [-1, 2, 9, 20, 4, -50, 20, 35, 45]

# fazendo a junção das duas listas só que determinadas pela lista de tamanho menor
juncao_a_b = zip(lista_a, lista_b)

# list comprehension para fazer o serviço
lista_soma = [ele_a + ele_b for ele_a, ele_b in juncao_a_b]

# for para iteração
# for ele_a, ele_b in juncao_a_b:
#     ele_soma = ele_a + ele_b
#     lista_soma.append(ele_soma)

print(lista_soma)
