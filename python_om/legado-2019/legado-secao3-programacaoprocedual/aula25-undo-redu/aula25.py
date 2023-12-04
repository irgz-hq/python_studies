"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

# Vamos trabalhar com funções, nesse campo a gente vai definilas

# Definindo a função show_op para mostrar a lista atual
def show_op(todo_list):
    print(todo_list)

# Definindo a função de adicionar a tarefa a lista principal
def do_add(todo_list, tarefa):
    todo_list.append(tarefa)

# Definindo a função do_undo para retornar
def do_undo(todo_list, redo_list):

    if not todo_list:
        print('Nada a se fazer!')

    else:
        # aqui eu tiro o ultimo item da lista e armazeno na redo_list, isso vai me permitir
        # 'passear' por ela com undo e redo.
        last_todo = todo_list.pop()
        redo_list.append(last_todo)

# Definindo a função do_redo para avançar
def do_redo(todo_list, redo_list):

    if not redo_list:
        print('Nada a se fazer!')

    else:
        # aqui eu tiro o ultimo item da redo_list (que foi adicionado ao retirar com undo)
        # o que vai me permitir "passear" por ela com undo e redo.
        first_todo = redo_list.pop()
        todo_list.append(first_todo)

if __name__ == '__main__':

    todo_list = []
    redo_list = []

    while True:

        tarefa = input('Digite a tarefa, undo, redo, ls ou exit: ')

        if tarefa == 'ls':
            show_op(todo_list)

        elif tarefa == 'undo':
            do_undo(todo_list, redo_list)

        elif tarefa == 'redo':
            do_redo(todo_list, redo_list)

        elif tarefa == 'exit':
            break

        else:
            do_add(todo_list, tarefa)

    print('Programa encerrado')
