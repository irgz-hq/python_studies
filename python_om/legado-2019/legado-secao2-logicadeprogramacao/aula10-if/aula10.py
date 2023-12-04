if True:
    print("Essa frase eh verdadeira")
elif False:
    print("Essa tambem")
elif False:
    print("Essa nao eh")
else:
    print("Essa vai aparecer pq a anterior eh falsa")

# note que um verdadeiro ja pula os outros

# Operadores Relacionais

"""
== > >= < <= !=
"""
num_1 = float(input("Digite um numero! "))
num_2 = float(input("Digite outro numero! "))
expressao = num_1 >= num_2
if expressao:
    print(f"{num_1} eh maior ou igual a {num_2}")
else:
    print(f"{num_1} eh menor que {num_2}")
teste = int(input("Teste"))  #cuidado, """""" nao eh string, entao pode existir algo do tipo int("""30""")
print(teste)
