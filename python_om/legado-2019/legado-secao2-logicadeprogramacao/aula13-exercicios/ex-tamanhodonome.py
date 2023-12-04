"""
Escreve um programa que peça o nome do usuário e calcule o tamanho desse nome,
se o tamanho for menor que 4, informe que é pequeno, entre 4 e 6, normal e
maior que 6, é grande.
"""

nome = input("Qual o seu nome (maiúsculo)? ")
verificacao = nome.istitle() and nome.isalpha()
if not verificacao:

    print("Você não escreveu seu nome corretamente! ")

else:

    tamanho = len(nome)
    if tamanho < 4:
        print(f"Seu nome é pequeno, pois só tem {tamanho} letras. ")
    elif tamanho >= 4 and tamanho <= 6:
        print(f"Seu nome até que tem o tamanho normal, pois tem {tamanho} letras. ")
    else:
        print(f"Seu nome é grande, pois tem {tamanho} letras. ")
