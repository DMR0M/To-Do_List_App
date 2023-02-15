import streamlit as st
from todo_app_cli import functions


def add_todo():
    new_todo = st.session_state['new_todo']
    print(new_todo)


todos = functions.get_todos()

st.title('TO-DO List App')
st.subheader('My todo list app')
st.write('Increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
