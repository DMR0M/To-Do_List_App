todos: list = []

while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # Option to add todo

            todo = input('Enter a todo: ') + '\n'
            with open('todos.txt', 'r') as txt_f:
                todos = txt_f.readlines()
                todos.append(todo.title())
            with open('todos.txt', 'w') as txt_f:
                txt_f.writelines(todos)

        case 'show' | 'display':
            # Option to show todo-list

            with open('todos.txt', 'r') as txt_f:
                todos = txt_f.readlines()
            for idx, item in enumerate(todos, start=1):
                print(f'{idx} - {item.strip().title()}')

        case 'edit':
            # Option to edit a todo entry in the todo-list

            order = int(input('Number of the todo to exit: '))
            print(todos[order-1])

            with open('todos.txt', 'r') as txt_f:
                todos = txt_f.readlines()

            edit_todo = input('Type what to do: ')
            todos[order-1] = f'{edit_todo}\n'

            with open('todos.txt', 'w') as txt_f:
                txt_f.writelines(todos)

            print('Updated Successfully')

        case 'complete':
            # Option to clear a completed todo entry in the todo-list

            to_remove = int(input('Type the number of the todo to remove: '))
            with open('todos.txt', 'r') as txt_f:
                todos = txt_f.readlines()

            print(f'Completed {todos[to_remove-1].strip()}')
            todos.pop(to_remove-1)

            with open('todos.txt', 'w') as txt_f:
                txt_f.writelines(todos)

        case 'exit':
            # Option to exit the program

            break
        case _:
            # Catch all unknown inputs

            print('Unknown Command')

