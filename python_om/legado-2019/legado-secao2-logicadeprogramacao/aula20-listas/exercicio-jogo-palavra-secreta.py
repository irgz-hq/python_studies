
# Jogo da palavra secreta. Determine uma palavra para ser advinhada pelo jogador.


palavra_secreta = 'eletromagnetismo'
chances = 3

# aqui, temos uma lista dinâmica.
digitadas_correta = []

print(f'Bem vindo ao jogo da palavra secreta, você tem {chances} chances para acertar a palavra secreta!')
while True:

    while True:
        letra_dig = input(f'Digite uma letra para tentar acertar a palavra secreta: ')
        if len(letra_dig) > 1 or letra_dig.isnumeric():
            print('Digite somente uma letra! ')
        else:
            break

    # se a letra_dig estiver na palavra secreta ele informa que você acertou e adiciona essa
    # letra na variavel digitadas_correta.

    if letra_dig in palavra_secreta:
        print('UHUUUL, você acertou a letra.')
        digitadas_correta.append(letra_dig)

    # caso contrário, ele diminui uma chance e informa que você não acertou.
    else:
        chances -= 1
        print(f'AFFZ, você não acertou a letra :(.')

    # aqui é onde tá a parte mais legal, definimos a palavra final como sendo vazia,
    # em toda a repetição isso vai acontecer.

    palavra_final = ''

    # aqui definimos da seguinte forma, para uma letra na palavra_secreta (lembrando que estamos
    # iterando toda palavra_secreta), verifique se ela foi armazenada em digitadas_correta,
    # se sim, mostre ela na palavra_final, se n, escreva um * no lugar.

    for letra in palavra_secreta:

        if letra in digitadas_correta:
            palavra_final += letra
        else:
            palavra_final += '*'

    # aqui, basicamente verificamos se ele ganhou, se ainda tem chances ou se perdeu.

    if palavra_final == palavra_secreta:
        print(f'Parabéns, você ganhou!!! A palavra secreta é {palavra_final}! ')
        break
    elif not chances > 0:
        print(f'Você perdeu! ')
        break
    else:
        print(f'A palavra secreta está assim: {palavra_final}, você ainda tem {chances} chances. ')
        print()
