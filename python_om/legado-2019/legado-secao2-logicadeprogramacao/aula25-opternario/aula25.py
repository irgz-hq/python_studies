
idade = int(input('Qual a sua idade? '))

msg = 'Você é maior de idade!' if idade >= 18 else 'Vocé é menor de idade! '
print(msg)

nome = input('Digite seu nome: ')
print(nome or 'Você não digitou nada =(')

a = 0
b = None
c = False
d = []
e = {}
f = 7
g = 'João'
variavel = a or b or c or d or e or f or g
print(variavel)