# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):

    resultado = 1
    for numero in args:
        resultado *= numero

    return resultado


print(multiplica(2, 3, 4))

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

num = float(input('Digite um número: '))

def par_ou_impar(numero):

    if numero % 2 == 0:
        print(f'O {numero} eh par')

    else:
        print(f'O {numero} eh ímpar')

par_ou_impar(num)

