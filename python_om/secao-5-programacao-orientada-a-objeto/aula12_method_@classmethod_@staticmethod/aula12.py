# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # setter, settando o user
    def set_user(self, user):
        self.user = user

    # setter, settando o password
    def set_password(self, password):
        self.password = password

    # classmethod para settar o usuario e a senha
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        # como se fosse um self.user...
        connection.user = user
        connection.password = password
        return connection

    # funcao dentro da classe que nao tem acesso nem a cls e nem a self
    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection()

# usando o class method para criar uma instancia ja settada
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')

print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)