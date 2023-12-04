
variavel = ['Luiz', 'AJoão', 'Maria']
for nome in variavel:
    if nome.lower().startswith('j'):
        print(nome, 'começa com J!')
    else:
        print(nome, 'não começa com J!')

# O else aqui tem a mesma função do while, só n será executado se encontrar a
# a palavra break.

for nome in variavel:
    if nome.lower().startswith('j'):
        print('existe um nome que começa com J!')
        break
else:
    print('Não existe um nome que começe com J!')
    