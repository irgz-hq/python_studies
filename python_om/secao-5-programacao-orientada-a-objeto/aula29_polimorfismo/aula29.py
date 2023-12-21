# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    # especificando o tipo é o L do solid
    @abstractmethod    
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando:', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando:', self.mensagem)
        return True
    
"""
Quando você especifica o tipo de argumento como Notificacao, você está
indicando que a função espera um objeto que seja uma instância da classe
Notificacao ou de qualquer classe derivada (subclasse) de Notificacao. 
Isso inclui objetos de classes filhas (subclasses) de Notificacao.
"""
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)

    

