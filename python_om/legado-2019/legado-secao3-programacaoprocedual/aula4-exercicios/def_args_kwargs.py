"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

# def ola_mundo():
#     return 'Olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# print(ola_mundo())

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""

# Aqui vem a função mestre
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

# Função mais simples com somente um parâmetro de assinatura
def fala_oi(nome):
    return f'Oi {nome}'

# Função mais complexa que a anterior com dois parâmetros de assinatura
def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

# Com args e kwargs ele consegue construir a função mestre em que ela
# suporta tanto a primeira função como a segunda.
executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
