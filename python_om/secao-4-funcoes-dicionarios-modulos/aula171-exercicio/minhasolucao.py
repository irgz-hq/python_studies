"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

l3 = list(zip(l1, l2))

# aqui serve para considerar zero os valores ausentes
# l3 = list(zip_longest(l1, l2, fillvalue=0))

resultado = [i[0] + i[1] for i in l3]
print(l3, resultado)
