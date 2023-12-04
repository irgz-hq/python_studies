"""
Fazer um programa que tenha dois contadores, um que conte progressivamente
e o outro que conte regressivamente. Usar os laços for e while.
"""

contador_p = 0
contador_r = 10

while contador_p <= 10:
    print(contador_p, contador_r)
    contador_p += 1
    contador_r -= 1

print()

for p, r in enumerate(range(10, 0, -1)):
    print(p, r)

lista = range(10,0,-1)
print(lista)
