"""
Faça um programa que peça a hora ao usuário e baseado nisso, faça a saudação
baseada.
"""
hora = input("Digite a hora: ")
verificacao = hora.isnumeric() and len(hora) <= 2
hora = int(hora)
verificacao2 = hora < 24
if verificacao and verificacao2:

    bomdia = hora <= 11
    boatarde = hora <= 17
    # boanoite = hora >= 18 and hora <= 23 nao precisa

    if bomdia:
        print("Bom dia! ")
    elif boatarde:
        print("Boa tarde!")
    else:
        print("Boa noite! ")

else:
    print("Você não digitou a hora corretamente.")
