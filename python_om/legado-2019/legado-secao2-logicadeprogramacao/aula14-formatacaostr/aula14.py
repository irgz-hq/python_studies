'''
Formatando variáveis com modificadores.

:s - Texto (str)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d, f)

> - ESQUERDA
> - DIREITA
^- CENTRO
'''

var_1 = 2
var_2 = 4521
print(f'{var_1:0>10}')  # variavel vai ta a direita do preenchimento
print(f'{var_2:0<10}')  # variavel vai ta a esquerda do preenchimento
print(f'{var_2:.1f}')  # quantidade de pontos flutuantes
var_3 = 'Luigui Augusto'
print(len(var_3),f'{var_3:#^30}')  # completar trinta caracteres só que a variavel vai estar no meio
nome = 'Lugui'
sobrenome = 'Augusto'
print('{0:$^50}{1:%^50}'.format(nome, sobrenome))  # os numeros dentro das chaves são os índices
nome = 'nOMe ALEaTorIo da siLvA'
print(nome.title())
print(nome.upper())
print(nome.lower())