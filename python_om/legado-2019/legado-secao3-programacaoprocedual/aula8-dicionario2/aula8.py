perguntas = {
    'pergunta 1': {
        'pergunta' : 'quanto é 2+2? ',
        'opções' : {'a' : '1', 'b' : '4', 'c' : '5'},
        'resposta' : 'b'
    },
    'pergunta 2': {
        'pergunta' : 'quanto é 3*2? ',
        'opções' : {'a' : '6', 'b' : '4', 'c' : '5'},
        'resposta' : 'a'
    },
}

acertos = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['opções'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite a sua resposta: ')

    if resposta_usuario == pv['resposta']:
        print('Você acertou! ')
        acertos += 1
    else:
        print('Você errou! ')

    porcentagem = acertos/len(perguntas) * 100
print(f'Sua porcentagem de acerto é {porcentagem}%. ')