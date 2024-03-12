import functions
import PySimpleGUI as gui


label = gui.Text('Enter a new todo')
input_box = gui.InputText(tooltip="Enter a new todo")
add_button = gui.Button('Add', tooltip="Add todo")

window = gui.Window('Todo App', layout=[[label], [input_box, add_button]], margins=(100, 70))
window.read()
window.close()