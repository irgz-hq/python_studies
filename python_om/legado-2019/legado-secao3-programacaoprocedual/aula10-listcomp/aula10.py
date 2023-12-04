l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [2*v for v in l1]  # pode usar função para fazer esse tipo de operação aritmética

ex3 = [(v, v2) for v in l1 for v2 in range(3)]


l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)

ex5 = [(y,x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5['valor2'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0]
print(ex6)

ex7 = [v for v in l3 if v % 3 == 0 if v % 7 == 0]

print(ex7)

ex10 = [v for v in l3 if v % 3 == 0 and v % 7 == 0]

print(ex10)


ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]


# ex9 = [v if v % 3 == 0 and v % 7 == 0 for v in l3]
# print(ex9)
# não funciona dessa maneira --> SyntaxError: expected 'else' after 'if' expression

numeros = [1, 2, 3, 4, 5]
novos_numeros = [n for n in numeros]

novos_numeros_append = []

for num in numeros:
    novos_numeros_append.append(num)

print(novos_numeros, novos_numeros_append)


# cuidado com as posições dos if e for
ex11 = [v if v != 69 else ';)' for v in l3 if v % 2 != 0]
print(ex11)

ex12 = [ (x,y)
         if y != 2 else (x*100, y*100)
         for x in range(1,11) for y in range(1,6) if x != 2]
print(ex12)

string = 'Luigui Augusto'
nova_string = [v for v in string]
nova_string_junta = '#'.join(nova_string)
print(nova_string, nova_string_junta)

str = 'Luigui Augusto'
numero_de_letras = 2
nova_str = '$'.join([
    str[indice : indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)
])
print(nova_str)

# Desafio: primeira tentativa
# nomes = ['João', 'Maria', 'José', 'Helena', 'Felipe']
# novos_nomes = [m.lower().replace(m[-1], m[-1].upper()) for m in nomes]

# print(novos_nomes)

# Desafio: primeira tentativa
nomes = ['João', 'Maria', 'José', 'Helena', 'Felipe']
novos_nomes = [n[:-1].lower() + n[-1].upper() for n in nomes]
print(novos_nomes)
novos_nomes = [f'{n[:-1].lower()}{n[-1].upper()}' for n in nomes]
print(novos_nomes)


