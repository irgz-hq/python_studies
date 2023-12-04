"""
1 - Crie uma função que exiba uma saudação com os paramêtros saudacao e nome!
"""

def funcao(saudacao = 'Olá', nome = 'Usuário! '):
    print(saudacao, nome)

nome = input('Qual o seu nome? ')
saudacao = 'Olá'
variavel = funcao(saudacao, nome)


