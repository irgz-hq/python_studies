"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles!
"""

def soma(n1, n2, n3):
    n1 = n1 + n2 + n3
    return n1

print('Digite os três números que você quer somar: ')
numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

resultado = soma(numero1, numero2, numero3)
print(f'O valor da soma entre {numero1}, {numero2} e {numero3} é {resultado}! ')