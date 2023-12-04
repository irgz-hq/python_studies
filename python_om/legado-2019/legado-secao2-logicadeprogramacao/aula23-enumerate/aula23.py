lista = [
    ['Acerola', 'Manga', 'Caju'],
    ['Limão', 'Banana', 'Maracujá'],
    ['Mamão', 'Cajá', 'Laranja']
]

print(lista[2],lista[2][1])

enumerado = enumerate(lista,31)
print(enumerado)
enumerado = list(enumerado)
print(enumerado)

for v1, v2 in enumerado:
    print(v1, v2)