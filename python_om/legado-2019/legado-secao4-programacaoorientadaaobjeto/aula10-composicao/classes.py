class Clientes:

    # aqui eu defino minha classe principal em q ela pede o nome e a idade
    # o endereco vai ser um objeto adcionado depois
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    # aqui definimos um metodo para inserir o endereco
    def insere_endereco(self, cidade, estado):
        # note que aqui o que estamos inserindo é a classe Endereco, como um objeto
        self.enderecos.append(Endereco(cidade, estado))

    # aqui iteramos pelo objeto (classe) Endereco e pegamos a cidade e o estado
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO!')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO!')