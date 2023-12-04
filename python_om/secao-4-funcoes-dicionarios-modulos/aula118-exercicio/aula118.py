# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# Aqui eu to criando uma função que cria outra
def cria_funcao(multiplicador):

    # Aqui eu defino a funcao a partir do parametro que foi recebido
    # ao chamar cria_funcao
    def funcao_multiplica(numero):
        numero *= multiplicador

        # Aqui eu retorno o número em sí, mas só quando eu chamar ela de fato
        return numero

    # Aqui eu retorno a funcao
    return funcao_multiplica

# Diversos exemplos
f1=cria_funcao(1)
f2=cria_funcao(2)
f3=cria_funcao(3)

print(f1(3),f2(3),f3(3))
