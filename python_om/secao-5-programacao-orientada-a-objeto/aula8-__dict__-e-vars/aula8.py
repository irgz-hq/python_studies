# Atributos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        # se usar o self.ano_atual em return do get... o python vai buscar primeiro na instancia
        # e depois na classe
        # self.ano_atual = 2023
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p1.nome = 'EITA'
# deleta o atributo
# del p1.nome

# __dict__ eh o dicionario onde ficam armazenados os atributos da sua classe
print(p1.__dict__)
# funcao para demonstrar isso
print(vars(p1))

# esse dicionario pode ser mudado
p1.__dict__['outra'] = 'coisa'
print(vars(p1))
print(p1.outra)

# posso fazer isso tambem
dicionario = {'nome': 'EITA', 'idade': 35}
p2 = Pessoa(**dicionario)
print(vars(p2))