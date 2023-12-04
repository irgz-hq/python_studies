
# aqui eu inicio o decorador, esse decorador tem como função
# alterar a função da func_soma q é em vez de somar qualquer número
# pegar um numero e somar com dez
def decorador(func):
    # aqui eh nosso wropper que faz a mudança na função (ou encapsulamento)
    def wropper(c):
        func(c, 10)
    
    # aqui é obrigatório retornar o wropper
    return wropper

# aqui eu defino a soma junto com o decorador
@decorador
def func_soma(a, b):
    soma = a + b
    print(soma)

# aqui a gente chama a função pelo nome mas o nome real dela é a do encapsula-
# mento
func_soma(10)
print(func_soma.__name__)



