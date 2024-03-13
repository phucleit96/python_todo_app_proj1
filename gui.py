import functions
import PySimpleGUI as gui


label = gui.Text('Enter a new todo')
input_box = gui.InputText(tooltip="Enter a new todo", key="todo")
add_button = gui.Button('Add', tooltip="Add todo")

window = gui.Window('Todo App',
                    layout=[[label], [input_box, add_button]],
                    margins=(100, 70),
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+ '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break
window.close()