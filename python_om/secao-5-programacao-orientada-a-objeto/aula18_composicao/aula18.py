# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

# a diferenca para composicao a agregacao eh que quando vc apaga o todo
# todo, todas as partes desse todo some
# Exemplo: carrinho de compras, produtos que fazem parte do carrinho
# caso o carrinho suma, eles tbem somem

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # aqui eu estou criando a instancia de Endereco dentro da classe cliente
        # isso quer dizer que quando o cliente deixar de existir, a instancia de 
        # endereco tbem deixara de existir
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # método que eh acionado quanto um objeto esta prestes a ser apagado
    # finalizador
    def __del__(self):
        print('APAGANDO', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

cliente1.listar_enderecos()

# repare que esse só vai ser apagado depois que o código finalizar
endereco_externo = Endereco('Av Saudade', 12)

del cliente1

print('################# AQUI TERMINA O MEU CÓDIGO')