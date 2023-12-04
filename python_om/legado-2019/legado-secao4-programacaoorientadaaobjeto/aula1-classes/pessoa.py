from datetime import datetime

class Pessoa:

    # variavel da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # uma funcao dentro de uma classe chama-se método

    # metodo para criar as intancias, ou seja, atribuir caracteristicas a sua instancia
    # lembrando que o self (pode ser qualquer palavra) referencia ele mesmo.

    # para criar uma variavel da instancia, basta fazer o seguinte: p1.nome = "Luiz"
    # __init__ é um método pronto do Python
    def __init__(self, nome, idade, comendo=False, falando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade