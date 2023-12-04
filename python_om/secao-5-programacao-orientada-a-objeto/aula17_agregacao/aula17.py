# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

'''
Agregação: as duas coisas existem separadamente, mas juntas executam uma ação
Exemplo: carro e roda, ambos existem separadamente, mas só andam se estiverem juntos
'''

class Carrinho:
    def __init__(self):
        self._produtos = []
        # nem vou criar getter e setter

        # metodo do carrinho mas que precisa dos produtos
    def total(self):
        return sum([p.preco for p in self._produtos])
        
    def inserir_produtos(self, *produtos):

        # pode ser feito tbem
        # self._produtos.extend(produtos)
        # self._produtos += produto
        for produto in produtos:
            self._produtos.append(produto)

        # outro metodo
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())


