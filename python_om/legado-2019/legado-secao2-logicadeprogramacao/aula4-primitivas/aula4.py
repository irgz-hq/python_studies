"""
str = string = textos, ex: "this", 'this'...
int = integer = integer numbers, ex: 1, 2, 256, -100, -1...
float = real number, ex: 1.1, 100.23, -10.2...
bool = booleano/logical, ex: True/False 10 == 10 (True)
"""

print("Fulano", type("Fulado"))
print(-123, type(-123))
print(1.1, type(1.1))
print(10 == 10, type(10 == 10))
print("l" == "L", type("l" == "L"))

#aplicando em variaveis

l = 10
L = 10
print(l == L)
print("", bool(""))
print("Joao", bool("Joao"))

#type casting
print("10", type(int("10")))
# print("abc", type(int("abc"))) nao pode!
# print("10.1", type(int("10.1"))) nao pode!
print("10", type(float("10")), float("10"))

# Exercicio

# Nome
print("Luigui", type("Luigui"))

# Idade
print("25", "anos", type("25"))

# Altura
print("1.77", type("1.77"))

# Eh maior de idade?
print(25>18, type("bool(25>18)"))
