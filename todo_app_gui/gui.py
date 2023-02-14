from todo_app_cli import functions
import PySimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_btn = sg.Button('Add')


# GUI Title
# Main Window
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_btn]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = f"{values['todo']}\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Show":
            pass
        case sg.WIN_CLOSED:
            break

window.close()
