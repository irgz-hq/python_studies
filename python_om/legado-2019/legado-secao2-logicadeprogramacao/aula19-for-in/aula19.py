'''
For in em python
Iterando strings com for
Função range(start, limite, step)
'''

'''
Pelo que entendi, o for in serve para comandos do tipo iteração de strings, não
totalmente iguais, mas pelo menos parecidos.
'''

'''
break = termina o laço
continue = pula para o próximo laço
'''

frase = 'O rato roeu a roupa do rei de roma!'
nova_frase = ''
for n in frase:
    print(n)
    nova_frase += n
print(nova_frase)

print('####################')

frase = 'Python'
nova_frase = ''

for n in frase:

    if n == 't':
        continue  # ingora o if
        nova_frase = nova_frase + n.upper()

    elif n == 'h':
        nova_frase += n.upper()
        break  # quenra o loop
    else:
        nova_frase += n
print(nova_frase)
