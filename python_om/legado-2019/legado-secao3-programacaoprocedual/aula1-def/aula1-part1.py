"""
definição de funções a partir do def.
"""


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('á', 'a')  # Substituir o dígito por outro
    nome = nome.replace('a', '@')
    print(msg, nome)

saudacao()
saudacao('Hello', 'Zé Manuel')
