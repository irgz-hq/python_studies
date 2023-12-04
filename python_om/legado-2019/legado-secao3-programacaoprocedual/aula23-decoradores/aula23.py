from time import time


# Recebe a função
def velocidade(funcao):

    # Aqui entra a função slave para calcular o tempo de execução
    def interna(*args,**kwargs):

        # Inicia o time
        start_time = time()

        # Executa a função
        resultado = funcao(*args, **kwargs)

        # Guarda o time final da execução
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para ser executar.')
        return resultado
    return interna

"""
Os decoradores servem, principalmente, para adicionar recursos a funções já existentes.
"""

# Aqui estamos decorando a função
@velocidade
def demora():
    for i in range(10):
        print(i, end='')

demora()
