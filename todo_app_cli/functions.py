import os
# import datetime
import time

FILE_PATH = os.path.join(os.getcwd(), 'todo_app_cli', 'todos.txt')
custom_dformat = time.strftime('%m-%d-%Y')


def get_date():
    return custom_dformat


# Function to get the list from the txt file
def get_todos(file_path=FILE_PATH) -> list[str]:
    """Read a text file and return the list of to-do items"""
    with open(file_path, 'r') as txt_file:
        return txt_file.readlines()


# Function to write to the txt file
def write_todos(file_path: str, todos_arg: list) -> None:
    """Update the text file by writing the list of to-do items"""
    with open(file_path, 'w') as txt_file:
        txt_file.writelines(todos_arg)


WARNING_MESSAGE_1 = """###################################
WARNING:
Please enter the todo-list number 
of the todo you like to edit
###################################
"""

WARNING_MESSAGE_2 = """###################################
WARNING:
Item number is not in the todo-list
###################################
"""

if __name__ == '__main__':
    print(FILE_PATH)
    print(custom_dformat)