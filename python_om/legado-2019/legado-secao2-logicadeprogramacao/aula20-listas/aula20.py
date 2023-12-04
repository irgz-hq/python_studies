
# contador = 0
# tamanho = 15
# lista = dict()
# while contador < tamanho:
#     lista[contador] = contador
#     print(lista[contador])
#     contador += 1
# print(lista)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)
l1.extend(l2)
l4 = l1
print(l4)
l4.append(2000)  # adiciona um valor ao último índice da lista
l4.insert(1, 1500)  # adiciona um valor ao índice mencionado
print(l4)
l4.pop(1)  # remove o índice selecionado
print(l4)

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l5[2:7])
print(l5)

print(max(l5))
print(min(l5))

l2 = list(range(0, 10))
print(l2)
