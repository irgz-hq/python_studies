try:
    print(a)
except NameError as erro:
    print('Erro:',erro)

except IndexError as erro:
    print('Erro de índice ou chave')

except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu código foi executado corretamente.')
finally:
    print('Vai ser executado sempre (útil para fechar um arquivo mesmo que ocorra erro)')

print('Bora continuar')

# note que para descobrir o tipo de erro que você quer colocar no excep, basta digitar erro
# e ver as opções.