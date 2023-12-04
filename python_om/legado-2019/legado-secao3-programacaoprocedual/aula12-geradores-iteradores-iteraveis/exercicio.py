
carrinho = []

carrinho.append(('produto 1', 30.5))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))


# Desempacotando

total = sum([n for x, n in carrinho])
print(total)