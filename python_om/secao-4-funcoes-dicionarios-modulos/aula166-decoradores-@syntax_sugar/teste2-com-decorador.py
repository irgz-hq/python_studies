# aqui eu criei esse fabrica_decoradores para ter um escopo para acessar
# o numero que eu preciso para criar o decorador


def fabrica_decoradores(num=1):
    def decoradora(funcao):
        def interna(x):
            return funcao(x, num)
        return interna
    return decoradora
    





@fabrica_decoradores(2)
def multiplica(x, y):
    return x*y


def soma(x, y):
    return x+y

print(f"{multiplica(3)} e o nome eh {multiplica.__name__}")