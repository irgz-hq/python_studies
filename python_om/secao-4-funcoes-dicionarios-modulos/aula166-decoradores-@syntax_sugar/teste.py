# aqui vou criar uma funcao que multiplica dois numeros
def multiplica(x, y):
    resultado = x * y
    return resultado


def soma(x, y):
    resultado = x + y
    return resultado

# aqui eu vou criar uma funcao decoradora para fazer com que a minha funcao
# multiplique sempre por um numero qualquer


def decorador(func, num):
    def interna(x):
        resultado = func(x, num)
        return resultado
    return interna
# preste atencao no nome da funcao que se tornou interna

multiplicacao = decorador(multiplica, 5)
print("aqui a funcao ja esta decorada para multiplicar por 5")
print(f"noma da funcao eh {multiplicacao.__name__} e o resultado {multiplicacao(10)}")

somando = decorador(soma, 3)
print("aqui a funcao ja esta decorada para somar com 3")
print(f"noma da funcao eh {somando.__name__} e o resultado {somando(10)}")
