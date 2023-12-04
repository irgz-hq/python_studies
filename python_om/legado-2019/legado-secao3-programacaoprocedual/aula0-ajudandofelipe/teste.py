numero = float(input('Digite um número: '))

if numero > 10 and numero < 20:
    print('Número entre 10 e 20!')
else:
    print('Condição não satisfeita')

print('---------')

if not numero > 10 or not numero < 20:
    print('Condição não satisfeita')
else:
    print('Número entre 10 e 20!')

print('---------')

