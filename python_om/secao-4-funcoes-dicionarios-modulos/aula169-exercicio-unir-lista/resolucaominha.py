# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(list1, list2):
    nova_lista = []
    contador = 0
    if len(list1) <= len(list2):
        for cidade in list1:
            nova_lista.append((list1[contador], list2[contador]))
            contador += 1
    else:
        for cidade in list2:
            nova_lista.append((list1[contador], list2[contador]))
            contador += 1
    return nova_lista


print(zipper(lista1, lista2))
