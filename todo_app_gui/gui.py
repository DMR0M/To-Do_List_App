from todo_app_cli import functions
import PySimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_btn = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todo-items',
                      enable_events=True, size=(40, 12))     # Get the list from the functions module
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')


# Main Window
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_btn],
                           [list_box, edit_btn, complete_btn],
                           [exit_btn]],
                   font=('Verdana', 15))


while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo-items'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = f"{values['todo']}\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo-items'].update(values=todos)
        case 'Edit':
            todo_edit = values['todo-items'][0]
            new_todo = f"{values['todo']}\n"
            # Replace existing to-do item selected
            todos = functions.get_todos()
            todo_index = todos.index(todo_edit)
            todos[todo_index] = new_todo
            functions.write_todos(todos)
            window['todo-items'].update(values=todos)
        case 'Complete':
            todo_complete = values['todo-items'][0]
            todos = functions.get_todos()
            # Remove item from the to-do list
            todos.remove(todo_complete)
            functions.write_todos(todos)
            window['todo-items'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case 'todo-items':
            window['todo'].update(value=values['todo-items'][0])

        case sg.WIN_CLOSED:
            exit()
