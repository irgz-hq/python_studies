
variavel = 'valor'

def func():
    print(variavel)

def func2():
    # global variavel :: aqui vc define a variavel como global, mas n é considerado uma boa prática de programação.
    variavel = 'Outro valor'
    print(variavel)

def func3(args=None):
    args = args.replace('v', 'c')
    print(args)

func()
func2()
func3(args=variavel)
print(variavel)

#  Lembrando que você não pode tentar usar uma variavel global dentro de uma função e depois alterá-la.
