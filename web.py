import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.image(image="fulllogo.png", width=300)
st.title("PHUC'S TODO APP")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity!")

for todo in todos:
    st.checkbox(todo)
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

print('Hello')
st.session_state
