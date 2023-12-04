"""
count - Intertools
Atenção!!! count retorna um iterador e não um gerador
lembre-se, iterador é diferente de iterável que é diferente de gerador
"""

from itertools import count

contador = count(start=5, step=0.01)
# contador = count(start=5, step = 2)  inicia a partir do 5 e o passo é de 2 em 2
# o passo pode ser negativo também
# o contador pode ser usado como índice de uma lista, você faz isso com o zip

for i in contador:
    print(round(i,2))  # precisão do ponto flutuante
    if i >= 100:
        break

