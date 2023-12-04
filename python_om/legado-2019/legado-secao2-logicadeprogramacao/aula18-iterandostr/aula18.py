string = 'O rato roeu a roupa do rei de roma!'
tamanho = len(string)
contador = 0
letra_escolhida = input('Qual a letra que voçê quer deixar maiúscula? ')
nova_string = ''
letra = ''

while contador < tamanho:

    letra = string[contador]
    if letra == letra_escolhida:
        nova_string += letra.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
