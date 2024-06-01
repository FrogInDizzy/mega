import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

# Initialize session state for todos

if "todos" not in st.session_state:
    st.session_state["todos"] = functions.get_todos()

todos = st.session_state["todos"]

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{idx}")
    if checkbox:
        print(checkbox)
        todos.pop(idx)
        functions.write_todos(todos)
        st.session_state["todos"] = todos
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')