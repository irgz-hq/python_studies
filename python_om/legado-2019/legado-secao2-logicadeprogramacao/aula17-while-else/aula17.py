
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    else:
        contador += 1
        acumulador += contador
else:  # else do while: serve para caso n tenha um break (igual no if), ele não
       # sai do while e executa o else, caso tenho um break, ele n executa o
       # else.
    print('Cheguei no else!')
print('Isso sera executado!')
