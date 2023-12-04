# Existem várias maneiras de se abrir, ler, editar um arquivo. Aqui vamos mostrar as três principais
# https://docs.python.org/3/library/functions.html#open

# lembrando que cada comando que você dar é como se tivesse um cursor, ele vai pra linha final
# que o comando sinaliza e para fazer outras operações, você precisa reposicionar o cursor com
# a função seek

file = open('abc.txt', 'w+')  # declara a variável com a função open. Segundo parâmetro ver site!
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # primeiro parametro serve para indicar a linha (offset e hence) (2 caractere pra frente)
                 # ence é a posição relativa aonde o cursor já está
print('lendo linhas')
print(file.read())
print('##########')
file.close()


