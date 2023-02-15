import streamlit as st
from todo_app_cli import functions

todos = functions.get_todos()

st.title('TO-DO List App')
st.subheader('My todo list app')
st.write('Increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo...')
