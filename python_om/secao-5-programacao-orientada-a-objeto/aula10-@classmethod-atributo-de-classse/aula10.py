# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # esse decorador faz com que eu possa chamar a minha classe sem passar self
    # mas eu preciso receber um parametro que eh a propria classe ou cls
    # lembrando que voce nao tem self no classmethod mas ele ta na classe, entao
    # vc usa normalmente eles la no __init__ e eles sao incorporados a sua nova
    # instancia (como tem que ser)
    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    # ele serve para criar uma determinada instancia (factory) ja com algum parametro
    # fixo, ou seja, um metodo para criar instancias fixas, nesse caso estou criando
    # uma pessoa com qualquer nome mas sempre com 50 anos de idade.
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('João', 34)

# aqui eu uso o classmethod para criar uma pessoa com 50 anos
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(20)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

