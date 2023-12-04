# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


# essa eh a funcao decoradora
# ela pega a funcao que eh inverter string e retorna a interna, na interna 
# a funcao inverter str ta dentro dela, mas agora ela checa se tudo eh string
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        # checando se eh string
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

# funcao que eu quero decorar, ela inverte uma string
def inverte_string(string):
    return string[::-1]

# verifica se eh string
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)