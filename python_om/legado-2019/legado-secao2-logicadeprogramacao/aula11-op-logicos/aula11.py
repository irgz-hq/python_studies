"""
Operadores logicos

and, or, not, in, not in
"""

# Usando and e or

var1 = input("Digite uma variavel: ")
var2 = input("Digite a segunda variavel ")
var_comp1 = input("Digite a primeira variavel a comparar: ")
var_comp2 = input("Digite a segunda variavel a comparar: ")

comparacao = var1 == var_comp1 and var2 == var_comp2
if comparacao:
    print(f"{var1} = {var_comp1} e {var2} = {var_comp2}. ")
else:
    comparacao = var1 == var_comp1 or var2 == var_comp2
    if comparacao:
        print(f"{var1} = {var_comp1} ou {var2} = {var_comp2}. ")
    else:
        print("todas as variaveis diferentes")

# Usando o not

var1 = input("Digite um numero: ")
var2 = input("Digite um segundo numero variavel ")

comparacao = var1 >= var2
if not comparacao:
    print(f"{var1} eh menor que {var2}")
else:
    print(f"{var1} eh maior ou igual a {var2}")

# Usando o in

var1 = input("Digite uma sequencia de numeros e letras: ")
var2 = input("Digite uma sequencia de numeros e letras que voce queira encontrar na ultima variavel: ")

comparacao = var2 in var1

if not comparacao:
    print(f"nao contem {var2} na sequencia {var1}")
else:
    print(f"contem {var2} na sequencia {var1}")

comparacao = var2 not in var1

var1 = input("Digite uma sequencia de numeros e letras: ")
var2 = input("Digite uma sequencia de numeros e letras que voce queira encontrar na ultima variavel: ")

if comparacao:
    print(f"nao contem {var2} na sequencia {var1}")
else:
    print(f"contem {var2} na sequencia {var1}")