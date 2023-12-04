
lista = []
lista_refazer = []

def printar_lista(lista):
    print("TAREFAS")
    for tarefa in lista:
        print(tarefa)
    print()

while True:

    # comandos refazer, desfazer e listar

    comando = input("lista de comandos: refazer, desfazer ou listar\n"
                "digite um comando ou uma tarefa: ")
    print("##############")
    print(comando)
    # if para sair
    if comando == "sair":
        break

    # if para o comando listar
    elif comando == "listar":
        if not lista == []:
            printar_lista(lista)

        else:
            print('nada a mostrar\n')

    # if para o comando desfazer
    elif comando == "desfazer":
        if not lista == []:
            desfazer = lista.pop()
            lista_refazer.append(desfazer)
            
        else:
            print('nada a desfazer\n')

    # if para o comando refazer
    elif comando == "refazer":
        if not lista_refazer == []:
            refazer = lista_refazer.pop()
            lista.append(refazer)
        
        else:
            print('nada a refazer\n')
    else:
        lista.append(comando)



            
    
