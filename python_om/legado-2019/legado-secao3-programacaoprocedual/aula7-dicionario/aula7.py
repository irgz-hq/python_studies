"""
Dicionário vc abre com chaves e vc dá nome aos índices!
"""

d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'
d2 = dict(chave1 = 'Valor da chave 1', chave2 = 'Valor da chave 2')
d3 = {'chave':'valor', 'chave':'valor', 'chave':'valor', 'chave':'valor real da chave', }

print(d1)
print(d1['chave1'], d1['nova_chave'])
print(d2)
print('d3',d3)

d4 = {
    'str' : 'valor',
    123 : 'outro valor',
          (1,2,3) : 'Tupla'
}

print(d4[(1,2,3)])

# O interessante de dicionários é que os índices podem ir pra um comando for, if, while...

if 'não existe' not in d4:
    print('Não existe esse índice')

print(d4.get('não existe'))  # pode fazer isso para o python não achar uma exceção

d4.update({'índice do update': 'índicizada do updatezada'})  # serve para atualizar o dicionário
print(d4['índice do update'])

del d4['índice do update']  # deleta

print('índice do update' in d4)
print((1,2,3) in d4)
print((1,2,3) in d4.keys())
print((1,2,3) in d4.values())
print(len(d4))

#  iterando sobre os dicionários

d5 = {
    'chave1' : 'valor chave 1',
    'chave2' : 'valor chave 2',
    'chave3' : 'valor chave 3',
}

for i in d5.keys():
    print(i)

for i in d5.values():
    print(i)

for i in d5.items():
    print(i)

# dicionário dentro de dicionário
print('Dicionário dentro de dicionário')

clientes = {
    'cliente1' : {'nome': 'João', 'sobrenome' : 'Felipe'},
    'cliente2' : {'nome': 'Luigui', 'sobrenome' : 'Augusto'},
    'cliente3' : {'nome': 'Joilza', 'sobrenome' : 'Soares'},
    'cliente4' : {'nome': 'Larissa', 'sobrenome' : 'Thaynan'},
    'cliente5' : {'nome': 'Ivanildo', 'sobrenome' : 'Soares'},
}

# não esquecer do .items() pelo amor de jah
for clientes_k, clientes_l in clientes.items():
    print(clientes_k)
    for nome, sobrenome in clientes_l.items():
        print(f'\tnome:{nome}', f'\tsobrenome={sobrenome}')

# atribuir valores do tipo dicionário para outra variavel

print('cópias')
v = d1.copy()
v['chave1'] = 'Valor da chave v'
print(d1, v)

print('cópias razas')
d6 = {1 : 'a', 2 : 2, 3 : 3, 'a' : {'b' : 'c', 'd' : 'e'},}
m = d6.copy()  # cópia vazia

m[1] = 'Luiz'
m['a']['b'] = 'balacubacu'
print(d6)
print()
print(m)

# observe que ele trocou nas duas, isso pq é uma cópia raza, para resolver isso tem q importar o módulo
# copy e usar o copy.deepcopy(d6). (tuplas não são alteradas)

d6 = {1 : 'a', 2 : 2, 3 : 3, 'a' : ('c', 'e')}
m = d6.copy()  # cópia vazia

m[1] = 'Luiz'
m['a'] = ('e','c')  # pode alternar as tuplas
print(d6)
print()
print(m)

# podemos converter listas com listas dentro em dicionário, assim como tuplas com
# listas dentro ou listas com tuplas dentro.
# podemos concatenar dicionários e usar as funções de edições de listas para dicionários (cuidado!
# não tenho certeza) como por exemplo o pop('chave especificada') e popitem().
