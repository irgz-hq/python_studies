# import sys ########## print(sys.platform)
from sys import platform as os
print(os)

from random import randint as aleatorio

print(aleatorio(1,20))

# para criar módulos, basta criar um novo arquivo .py e importar. Caso n queira executar algo dentro do módulo
# use o __name__ que ele vai retornar __main__ se tiver sendo executado como principal ou vai retornar o nome
# caso esteja sendo executado em outro programa.