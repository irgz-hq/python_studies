from abc import ABC, abstractmethod

class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    # como os atributos estao com _, precisamos do getter pra pegar esses valores
    # e o setter caso queira manipula-los

    #aqui esta o getter
    #note que agora a funcao virou um atributo para ser chamado
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    #aqui está o setter
    @saldo.setter
    def saldo(self, valor):
        #aqui isinstance serve para ver se o valor eh uma instancia de alguma dessas classes.
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numerico")

        self.saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numerico")
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    #todas as contas precisam sacar, mas dependendo do tipo de conta, cada uma vai ter
    #um tipo de saque diferente, é aí que entra o abstractmethod
    @abstractmethod
    def sacar(self, valor):
        pass