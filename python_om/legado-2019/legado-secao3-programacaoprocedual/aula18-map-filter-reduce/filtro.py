from dados import pessoas, lista, produtos

# a função filter é similar a map só que a diferença entre elas é que a filter vai retornar
# ou verdadeiro ou falso para a expressão que você quer falar.

# exemplo abaixo, se x for maior que 5 (na função lambda) então ele será adicionado ao novo
# iterator, se n, ele n é considerado.

# nova_lista =filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]

print(list(nova_lista))

#######################################################

# queremos filtrar os preços > 50.

# novos_precos = filter(lambda p: p['preco'] > 10, produtos)  # com funcao lambda

def filtra_preco(p):
    if p['preco'] > 10:
        return True
    else:
        return False
    # se n tivesse o else, ela voltaria None, tbem funcionaria

novos_precos = filter(filtra_preco, produtos)

for item in novos_precos:
    print(item)

# podemos usar o filter como map tbem, n é recomendável

def filtra_preco2(p):
    if p['preco'] > 10:
       p['eh_caro'] = 'Verdade ou', True
    return True

novos_precos2 = filter(filtra_preco2, produtos)

for item2 in novos_precos2:
    print(item2)