import functions
import PySimpleGUI as gui
import time

gui.theme("LightBlue")
image = gui.Image('fulllogo.png', subsample=9, zoom=2)

clock = gui.Text('', key='clock', font=('Helvetica', 12, 'bold'))
label = gui.Text('Enter a new todo', font=('Helvetica', 12, 'bold'))
input_box = gui.InputText(tooltip="Enter a new todo", key="todo", size=(41, 1))
add_button = gui.Button('Add', tooltip="Add todo")
list_box = gui.Listbox(values=functions.get_todos(), size=(40, 10), enable_events=True, key='todos')
edit_button = gui.Button('Edit', tooltip="Edit todo")
complete_button = gui.Button('Complete', tooltip="Finish a task")
exit_button = gui.Button('Exit', button_color=('white', 'red'))

col1 = gui.Column([[clock],[image]])
col2 = gui.Column([[label, add_button, edit_button, complete_button, exit_button], [input_box], [list_box]])

layout = [[col1, col2]]

window = gui.Window('Todo App',
                    layout=layout,
                    margins=(60, 40),
                    font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=10)
    if event in (gui.WINDOW_CLOSED, 'Exit'):  # add this line
        break  # add this line
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup('Please select an item first!', font=('Helvetica', 17))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                gui.popup('Please select an item first!', font=('Helvetica', 17))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break

window.close()
