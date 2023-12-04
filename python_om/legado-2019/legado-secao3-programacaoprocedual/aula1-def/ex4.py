"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função
for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
while True:
    condicao = input('Deseja sair do FizzBuzz (s/n)? ')
    if condicao == 's':
        break
    else:
        def FizzBuzz(num):
            if num % 3 == 0 and num % 5 == 0:
                return 'FizzBuzz'
            elif num % 3 == 0:
                return 'fizz'
            elif num % 5 == 0:
                return 'buzz'
            else:
                return num

    numero = int(input('Digite um número: '))
    resultado_novo = FizzBuzz(numero)
    print(resultado_novo)