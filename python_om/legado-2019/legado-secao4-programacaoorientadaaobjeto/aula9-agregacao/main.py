from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1800)
p3 = Produto('Tenis', 250)

carrinho.inserir_produto(p1)
carrinho.soma_total()
carrinho.inserir_produto(p2)
carrinho.soma_total()
carrinho.inserir_produto(p3)
carrinho.soma_total()
carrinho.lista_produto()
carrinho.soma_total()
