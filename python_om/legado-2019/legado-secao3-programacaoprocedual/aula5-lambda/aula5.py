lista = [
    ['p1', 5, 3], ['p2', 20, 4], ['p3', 15, 5], ['p4', 4, 1], ['p5', 9, 6]
]

def func(item):
    return item[2]  # aqui ele n referencia a lista mas sim o elemento da lista
                    # que vai ser considerado pra ser ordenado!

lista.sort(key=func, reverse=True) # função ordenar

print(lista)
print(func(lista))

print('abaixo é com o lambda! ')

lista_nova = [
    ['p1', 5, 3], ['p2', 20, 4], ['p3', 15, 5], ['p4', 4, 1], ['p5', 9, 6]
]
lista_sort = lista_nova
lista_sorted = lista_nova

lista_nova.sort(key=lambda item: item[1], reverse=True) # função ordenar

print(lista_nova)

print(sorted(lista_sorted, key=lambda i: i[1], reverse=True))
