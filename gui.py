import functions
import PySimpleGUI as gui


label = gui.Text('Enter a new todo')
input_box = gui.InputText(tooltip="Enter a new todo", key="todo")
add_button = gui.Button('Add', tooltip="Add todo")
list_box = gui.Listbox(values=functions.get_todos(), size=(50, 10), enable_events=True, key='todos')
edit_button = gui.Button('Edit', tooltip="Edit todo")

window = gui.Window('Todo App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    margins=(100, 70),
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break
window.close()