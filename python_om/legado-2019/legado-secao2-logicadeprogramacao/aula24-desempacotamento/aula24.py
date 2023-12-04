
lista = ['Laranja', 'Cajá', 'Acerola', 1, 2, 3, 4, 'sou o ultimo']
n1, *outra_lista, ultimo_da_lista = lista
print(n1, outra_lista, ultimo_da_lista)
# outro exemplo

n1, *outra_lista, n2, n3 = lista  # pode utilizar *_ para n utilizar o resto dos valores que você n se preocupa
print(n1, outra_lista, n2, n3)

# invertendo valores de variáveis

x = 10
y = 'João'
x, y = y, x
print(x, y)