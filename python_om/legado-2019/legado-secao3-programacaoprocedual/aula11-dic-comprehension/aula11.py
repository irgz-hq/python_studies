
lista = [
    ('chave1', 2),
    ('chave2', 3),
]
# lembrar do formato de dicionário
d1 = {x.upper(): y*2 for x, y in lista}

print(d1, type(d1))

# conjunto (set)

d2 = {x for x in range(10)}
print(d2, type(d2))

# Exemplo: quadrado

d3 = {f'numero_{x}': f'quadrado = {x**2}' for x in range(100)}
print(d3)