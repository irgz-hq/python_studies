"""
Importante!!! Se n usar o comando return dentro do def, ele não vai retornar
valor para uma variavel. Se n usar o return, ela só vai executar determidada
tarefa e n vai retornar nenhum valor
"""

# Aqui eu n estou retornando o valor de var.
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero!')
print(variavel)

# Aqui eu estou retornando o valor de var.
def funcao_2(var):
    return var
    # print('Qualquer coisa que tiver depois do return (dentro do def) n será executado!')

variavel_2 = funcao_2('Valor que eu quero!')
print(variavel_2)

# Exemplo: divisão por zero

def divisao(n1, n2):
    if not n2 == 0:
        n1 = n1/n2
        return n1
    else:
        n1 = 'Número ínvalido'  # Famosa tipagem dinâmica!
        return n1

variavel1 = int(input('Digite o primeiro número: '))
variavel2 = int(input('Digite o segundo número: '))
resultado = divisao(variavel1, variavel2)

# Lembrando que, o tipo da variavel quando chama a função é dado pelo return,
# caso n tenha return, é dado como tipo function.

print(resultado, type(resultado))

# Função retornando função

def f(var):
    print(var)

def dumb():
    return f

variavel3 = dumb()
variavel4 = dumb()('Printei!')  # Aqui vai printar

print(type(variavel3))
print(type(variavel4), variavel4)  # Aqui nao vai printar pq aqui eu n retornei

print(id(variavel3), id(f), id(variavel4))
