'''
* Split serve para dividir strings
* Join serve para juntar strings
* Enumerate serve para enumerar elementos de uma lista # iteráveis
* Função strip remove os espaços do início e fim da str
'''

string = 'O Brasil é o páis do futebol, o Brasil é penta.'
lista_1 = string.split(' ')  # a partir de ' ' que ele separa
lista_2 = string.split(',')  # separa a partir de ','

print(string)
print(lista_1)
print(lista_2)

for valor in lista_1:
    print(f'a palavra ({valor}) apareceu {lista_1.count(valor)}x na frase.')


string = 'O Brasil é penta.'
lista = string.split(' ')
string_2 = ' '.join(lista)
string_3 = '#'.join(lista)

print(string)
print(lista)
print(string_2)
print(string_3)

for indice, nome in enumerate(lista):
    print(indice, nome)

n1, n2, n3, n4 = lista
print(n4)
