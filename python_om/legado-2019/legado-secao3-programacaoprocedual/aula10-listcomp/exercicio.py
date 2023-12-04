"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
lista = [0123456789, 0123456789, 0123456789, 0123456789, 0123456789, 0123456789, 0123456789]
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789'
intervalo = 10
tamanho_str = len(string)

# lembre-se, você pode usar o for no list comp pra variavel que não esteja
# diretamente associada com o retorno para a lista

lista = [string[n:n + intervalo] for n in range(0, tamanho_str, 10)]
retorno = '.'.join(lista)
print(lista)
print(retorno)