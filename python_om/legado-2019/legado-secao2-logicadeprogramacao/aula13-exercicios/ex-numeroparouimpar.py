"""
 Escreve um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que nao é um número inteiro.
"""

numero = input("Digite um número inteiro para verificarmos se é par ou ímpar: ")

if numero.isnumeric():
    numero = int(numero)

    # Aqui, pegamos o menor inteiro da divisao por 2 e multiplicamos por 2 para
    # saber se eh par, se verificacao for menor (ou diferente) que numero,
    # entao é ímpar.

    # Detalhe, 50 == 50.0 é True!

    verificacao = numero % 2

    if verificacao == 0:
        print(f"O número {numero} é par! ")
    else:
        print(f"O número {numero} é ímpar! ")
else:
    print(f"Você não digitou um número inteiro :( ")
