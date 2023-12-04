
def divide_por_dois(y=2):
    def decoradora(funcao):
        def interna(x):
            return funcao(x, y)
        return interna
    return decoradora

def divide(x, y):
    if y == 0:
        print('não divido por zero')
        return

    return x/y

a = divide_por_dois()
b = a(divide)
print(b(4))


# variavel_decoradora = divide_por_dois()
# q = variavel_decoradora(divide)
#print(divide(2))

