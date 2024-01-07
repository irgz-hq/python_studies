# classe decoradora
class Vezes10:
    # recebe a funcao
    def __init__(self, funcao):
        self.funcao = funcao
    
    # recebe os argumentos da funcao quando se é chamada
    def __call__(self, x, y):
        return self.funcao(x,y)*10

@Vezes10
def multiplicar(x, y):
    multiplicacao = x*y
    return multiplicacao

print(multiplicar(2,3))
