"""
3 - Crie uma função que receba dois números. O primeiro é um valor e o segundo um
percentual. Retorne o valor do primeiro número somado do percentual do mesmo.
"""

def soma_percentual(numero, percentual):
    percentual /= 100
    numero +=  numero*percentual
    return numero

numero_novo = float(input('Digite um número: '))
percentual_novo = float(input('Digite o percentual a ser somado (em %): '))

resultado = soma_percentual(numero_novo, percentual_novo)
print(f'{numero_novo} mais {percentual_novo}% é {resultado}. ')