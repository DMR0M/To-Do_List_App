from functions import get_date, get_todos, write_todos
from functions import FILE_PATH, WARNING_MESSAGE_1, \
    WARNING_MESSAGE_2
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def main():
    # Show current date
    print(f'{Fore.WHITE}##############################################\n'
          f'{Fore.CYAN}Date: {get_date()}\n'
          f'{Fore.WHITE}##############################################\n')
    while True:
        user_action = input('Type add, show, edit, complete, or exit: ')
        user_action = user_action.strip()

        if user_action.startswith('add') or user_action.startswith('new'):
            # Option to add entry
            try:
                todo = f'{user_action[4:]}\n'
                # Load todo list
                todos = get_todos(file_path=FILE_PATH)
                todos.append(f'{todo.title()}')
                # Write todo list
                write_todos(file_path=FILE_PATH, todos_arg=todos)
                print(f'{Fore.GREEN}{Style.BRIGHT}Added a todo entry')
            except ValueError:
                print('Enter a valid todo entry')
                continue

        elif user_action.startswith('show') or user_action.startswith('display'):
            # Option to show list
            todos = get_todos()
            print(f'{Fore.YELLOW}{Style.BRIGHT}TODO-LIST: ')
            for idx, item in enumerate(todos, start=1):
                print(f'{Fore.YELLOW}{idx} - {Fore.WHITE}{item.strip().title()}\t')

        elif user_action.startswith('edit'):
            # Option to edit an entry
            try:
                order = int(user_action[5:])
                # Load todo list
                todos = get_todos()
                print(f'{Fore.CYAN}{Style.BRIGHT}Changing {todos[order - 1]}')
                edit_todo = input('Type what to do: ')
                todos[order - 1] = f'{edit_todo}\n'
                # Write todo list
                write_todos(file_path=FILE_PATH, todos_arg=todos)

            except ValueError:
                print(f'{Fore.RED}{WARNING_MESSAGE_1}')
                continue
            except IndexError:
                print(f'{Fore.RED}{WARNING_MESSAGE_2}')
                continue

            print(f'{Fore.GREEN}{Style.BRIGHT}Updated Successfully')

        elif user_action.startswith('complete'):
            # Option to clear a completed entry
            try:
                to_remove = int(user_action[9:])
                # Load todo list
                todos = get_todos()

                print(f'{Fore.RED}{Style.BRIGHT}Completed {todos[to_remove - 1].strip()}')
                todos.pop(to_remove - 1)
                # Write todo list
                write_todos(file_path=FILE_PATH, todos_arg=todos)
            except ValueError:
                print(f'{Fore.RED}{WARNING_MESSAGE_1}')
                continue
            except IndexError:
                print(f'{Fore.RED}{WARNING_MESSAGE_2}')
                continue

        elif user_action.startswith('exit'):
            # Option to exit the program
            break

        elif user_action.startswith('clear todos'):
            # Load todo list
            todos = get_todos()
            prompt = input('Are you sure you want to clear the todo-list? (y/n): ')
            todos.clear()

            # Write todo list
            write_todos(file_path=FILE_PATH, todos_arg=todos)
            print(f'{Fore.YELLOW}{Style.BRIGHT}Successfully cleared the todo-list')

        else:
            # Catch all unknown inputs
            print('Unknown Command')


if __name__ == '__main__':
    main()
