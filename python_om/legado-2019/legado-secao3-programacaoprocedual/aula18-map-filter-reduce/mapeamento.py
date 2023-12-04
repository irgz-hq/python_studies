from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x* 2, lista)  # pode ser feito assim
nova_lista = [x*2 for x in lista]

print(lista)
print(list(nova_lista))

# usando de fato a função map

# a função map pode ser usada no lugar de list comprehensions e vice e versa, mas
# a função map se destaca quando vc quer preservar o tipo do objeto (list, dict, set, etc)
# e só quer passar uma função no objeto, segue exemplo:

# aqui definimos uma função para ser passada no dicionario, vamos fazer isso usando a função map

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

# aqui usamos a função map para passar a função aumenta_preco (que retorna o mesmo dict)
# no dict produtos

novos_produtos = map(aumenta_preco, produtos)

# aqui printamos o novos_produtos (já que a func map retorna um iterador (talvez gerador?))

for p in novos_produtos:
    print(p)

print('########################################################################')
print()
print()
print()

# aqui definimos uma função para ser passada no dicionario, vamos fazer isso usando a função map
# note que a func cria uma key no dict "nova_idade"
def aumenta_idade(pes):
    pes['nova_idade'] = pes['idade'] + 1
    return pes

# passando a aumenta_idade em pessoas, note a adição da key
pessoas_idades = map(aumenta_idade, pessoas)

# printando pessoas_idades
for pess in pessoas_idades:
    print(pess)