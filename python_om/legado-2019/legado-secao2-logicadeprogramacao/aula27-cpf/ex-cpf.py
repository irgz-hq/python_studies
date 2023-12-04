"""
Algoritmo para calcular um cpf:

CPF = 093.529.524-05

0*10                                                #  0*11
9*9                                                 #  9*10
3*8                                                 #  3*9
5*7                                                 #  5*8
2*6                                                 #  2*7
9*5                                                 #  9*6
5*4                                                 #  5*5
2*3                                                 #  2*4
4*2                                                 #  4*3
                                                    #  b*2
    soma
11 - (soma % 11) = a                                    11 - (soma % 11) = c
a > 9 implica primeiro digito b = 0
se for menor, é o próprio dígito.                       digito 2 = c
"""



while True:

    cpf = input('Bem vindo ao validador de cpf, digite o seu cpf: ')
    cpf_formatado = ''

# Aqui vem a verificação dos digitos:

    if cpf.isnumeric() and len(cpf) == 11:
        break

    else:

# Laço para formatar o cpf caso tenha '.' ou '-':

        for digito in cpf:
            if digito == '.' or digito == '-':
                continue
            else:
                cpf_formatado += digito

        cpf = cpf_formatado

        if cpf.isnumeric and len(cpf) == 11:
            break
        else:
            print(f'{cpf} incorreto, digite novamente! ')

# Laço para fazer a validação do primeiro dígito do cpf:

fator = 10
contador = 0
cpf_vefiricador = cpf[0: 9]

for digito in cpf_vefiricador:
    if fator < 2:
        break
    else:
        contador += int(digito)*fator
        fator -= 1

conta = 11 - (contador % 11)

if conta > 9:
    cpf_vefiricador += '0'
else:
    cpf_vefiricador += str(conta)

# Laço para fazer encontrar o segundo dígio:

fator = 11
contador = 0

for digito in cpf_vefiricador:

    if fator < 2:
        break
    else:
        contador += int(digito) * fator
        fator -= 1

conta = 11 - (contador % 11)

if conta > 9:
    cpf_vefiricador += '0'
else:
    cpf_vefiricador += str(conta)

if cpf == cpf_vefiricador:
    print(f'O seu cpf: {cpf} está correto!')
else:
    print(f'O seu cpf: {cpf} não está correto =[, o cpf correto seria {cpf_vefiricador}! ')
