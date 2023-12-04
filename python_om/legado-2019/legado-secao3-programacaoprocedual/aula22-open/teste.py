
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > 10 and num2 > 10:
    print(f'Os número {num1} e {num2} é maior que 10.')
else:
    print('Um dos números é menor que 10! ')

print('Aqui vem a lógica de negação')

if not num1 > 10 or not num2 > 10:
    print('Um dos números é menor que 10! ')
else:
    print(f'Os número {num1} e {num2} é maior que 10.')