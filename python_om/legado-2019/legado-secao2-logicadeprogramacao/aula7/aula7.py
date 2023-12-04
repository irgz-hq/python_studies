nome = "Fulano"
idade = 25
peso = 80

print(f"{nome} tem {idade} anos e pesa {peso}kg.")
print("{} tem {} anos e pesa {}kg.".format(nome, idade, peso))
print("{0} {2} {1} {0} tem {1} anos e pesa {2}kg.".format(nome, idade, peso))
print("{i} {k} {j} {i} tem {j} anos e pesa {k}kg.".format(i = nome, j = idade, k = peso))

real = 10/3
print(real)
print(f"{real:.2f}")  #para o :.2f funcionar, tem que ser em str
print(f"{real:.5f}")
