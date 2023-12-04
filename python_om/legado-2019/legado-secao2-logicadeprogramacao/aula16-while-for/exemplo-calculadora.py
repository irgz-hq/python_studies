while True:
    situacao = input('Deseja sair da calculadora, [s]im ou [n]ão? ')
    if not situacao == 's' and not situacao == 'n':
        print('Você precisa digitar s ou n! ')
    elif situacao == 's':
        break
    else:
        while True:
            operacao = input('Que operação você deseja fazer ([+], [-], [*], [/]')
            num_1 = input('Digite o primeiro número: ')
            num_2 = input('Digite o segundo número: ')
            try:
                num_1 = float(num_1)
                num_2 = float(num_2)
                break
            except:
                print('Você não digitou um número! ')

        if operacao == '+':
            print(f'{num_1} + {num_2} = {num_1 + num_2}')
        elif operacao == '-':
            print(f'{num_1} - {num_2} = {num_1 - num_2}: ')
        elif operacao == '*':
            print(f'{num_1} * {num_2} = {num_1 * num_2}: ')
        elif operacao == '/':
            print(f'{num_1} / {num_2} = {num_1 / num_2}: ')
        else:
            print('Você não digitou uma operação válida! ')
