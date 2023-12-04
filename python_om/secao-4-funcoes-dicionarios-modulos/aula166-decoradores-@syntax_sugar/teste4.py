
def decorador(func):
    def interna(x):
        return func(x,2)
    return interna


@decorador
def soma(x,y):
    return x + y

print(soma(2))

