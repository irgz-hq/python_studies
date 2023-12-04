"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""

def func1(arg):
    print(arg)

def func2():
    return 'valor da função2'

func1(func2())
