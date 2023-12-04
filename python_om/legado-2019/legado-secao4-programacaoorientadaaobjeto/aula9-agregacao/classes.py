# agregacao eh um tipo de dependencia em que uma classe usa a outra mas ela
# depende dela para funcionar corretamente

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
        print(self.produtos)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print(total)

"""
note que vai uma classe para a lista self.produtos, e isso n tem problema nenhum,
note tbem que podemos chamar o valor desses produtos a qualquer momento com o for
"""

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

