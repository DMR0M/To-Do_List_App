from todo_app_cli import functions
import PySimpleGUI as sg


label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do')
add_btn = sg.Button('Add')


# GUI Title
# Main Window
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_btn]])
window.read()
window.close()
