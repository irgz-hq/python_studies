"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 1, 2],
    [16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
]


def acha_duplicado(lista):

    # aqui eu defino a lista para guardar os numeros que vou iterando
    numeros_checados = []

    # aqui eu vejo o tamanho da lista
    tam_lista = len(lista)

    # contador para contar quantos numeros peguei para comparar com o próximo
    contador = 0

    # for para iterar na lista
    for numero in lista:

        # contador começando em 1 pra pegar o elemento da lista com índice mairo
        # que o da numeros_acumulados
        contador += 1

        # if para verificar se já verifiquei tudo
        if contador == tam_lista:
            return -1

        # adicionando o primeiro numero da lista a lista de numeros checados
        numeros_checados.append(numero)

        # aqui eu chego se tem algum numero repetido e retorno este numero
        for numero in numeros_checados:

            if numero == lista[contador]:
                return numero


def acha_duplicado2(lista):

    # aqui basicamente eu uso a propriedade de que nao se repete o numero no set
    numeros_checados = set()
    contador = 0
    for numero in lista:
        contador += 1
        numeros_checados.add(numero)

        if contador > len(numeros_checados):
            return numero
    return -1

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(lista, acha_duplicado(lista), acha_duplicado2(lista), encontra_primeiro_duplicado(lista))

# verificar solução com set que eh bem mais facil
