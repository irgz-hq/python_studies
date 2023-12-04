# aqui eu vou definir um criador de decorador
def criador_decorador(a=1):
    # aqui eu defino o decorador em si
    def decorador(func):
        # aqui eu defino a minha funcao interna para dar um closure na func que
        # recebo como argumento
        def interna(x):
            #aqui eu retorno minha func em si
            return func(x,a)
        return interna
    return decorador


# aqui quando eu uso @criador_decorador() "com parenteses" ele vai retornar 
# decorador, e o decorador eh quem vai a funcao soma de fato como argumento

@criador_decorador(3)
def soma(x,y):
    return x + y

@criador_decorador(4)
def multiplica(x,y):
    return x*y

print(soma(2), multiplica(2))

# lembrando que a primeira funcao decoradora (seja ela vindo do return do closure de uma funcao ou nao)
# deve ter como argumento uma func