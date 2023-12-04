"""
Higher Order Functions
Funções de primeira classe
"""

# Função principal
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# Executa a função, note que o *args eh para empacotar os argumentos que irão
# na função principal, note que foi usado *args la no return, para desempacotar
def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)