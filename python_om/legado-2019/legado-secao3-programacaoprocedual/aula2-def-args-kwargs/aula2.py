"""
Funções (def) - args e kwargs
"""
"""
A partir do momento que você especifica o valor do parâmetro, você precisa especificar no
argumento de quando você chama a função! 
"""


def func(a1, a2, a3, a4, a5, nome='Zé', a6='João'):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


# funciona mas n é o ideal, é preciso especificar var = func(1, 2, 3, 4, 5, 'Luiz', '5')
# funciona mas n é o ideal! var = func(1, 2, 3, 4, 5)

var = func(1, 2, 3, 4, 5, nome='Maria', a6='6')

print(var)

lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')  # o * serve para desempacotar! O argumento sep serve para definir o separador!

# Usando o args

def func(*args):

    print(args)  # se n converter, ele retorna como uma tupla
    args = list(args)  # convertendo a tupla em lista para poder alterar
    print(args)
    args[-1] = 'Mudeeeei!'
    print(args[0], args[-1])

func(1,2,3,4,46)

# kwargs

def func2(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])  # se tiver certeza que nome e sobrenome existe, pode usar dessa forma.
    idade = kwargs.get('idade')  # Sempre utilizar dessa forma, quando n tiver certeza que você receberá a variavel.
    print(f'Sua idade é {idade}. ')
lista = [1,2,3,4,5]
lista2 = [11,12,13,14,15]
func2(*lista, lista2, nome='Luigui', sobrenome='Augusto', idade = 25)  # Mandando a lista desempacotada

# kwargs == key words args
