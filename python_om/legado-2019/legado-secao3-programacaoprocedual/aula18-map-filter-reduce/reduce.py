from dados import produtos, pessoas, lista
from functools import reduce

valor_inicial_ac = 0
# aqui temos que definir um acumulador, item_da_lista, antes dos dois pontos definimos
# o loop entre o acumulador e o item_da_lista, após os dois pontos definimos a operação
# que queremos executar (nesse caso item_da_lista + acumulador).

soma_lista = reduce(lambda acumulador, item_da_lista: item_da_lista + acumulador, lista, valor_inicial_ac)
print(soma_lista)

# aqui é o mesmo raciocínio, só que como estamos lidando com um dict, temos que especificar a chave
# no lado da operação.
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, valor_inicial_ac)
print(soma_precos)