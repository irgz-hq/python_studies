
alunos = [
    {'nome' : 'Felipe', 'nota' : 'A' },
    {'nome' : 'Luigui', 'nota' : 'A' },
    {'nome' : 'João', 'nota' : 'B' },
    {'nome' : 'José', 'nota' : 'C' },
    {'nome' : 'Maria', 'nota' : 'B' },
    {'nome' : 'Tatiana', 'nota' : 'C' },
    {'nome' : 'Fernando', 'nota' : 'D' },
    {'nome' : 'Paula', 'nota' : 'A' },
]

from itertools import groupby

# unção lambda para ajudar a agrupar pela nota,
# agora vamos agrupar por nota, para isso vamos utilizar a função gruopby

ordena = lambda item: item['nota']  # lambda para ordenar
alunos.sort(key=ordena)  # ordenar
alunos_agrupados = groupby(alunos, ordena)  # agrupar

for item1, item2 in alunos_agrupados:
    print(f'Agrupamento {item1}')
    print(f'{len(list(item2))} alunos tiraram nota {item1}!')


