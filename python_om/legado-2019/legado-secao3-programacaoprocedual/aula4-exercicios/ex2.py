"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça
a função1 executar duas funções que recebem um número diferente de argumentos.
"""

def func1(*args):
    print(args)

def func2(nome='José'):
    return nome

def func3(saudacao='Olá', sobrenome='Luiz'):
    return saudacao, sobrenome

func1(func2(), func3())
