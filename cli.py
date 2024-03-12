from functions import *
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:

    user_input = input("Type add, update, show, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = get_todos()

        todos.append(todo.title() + '\n')

        write_todos(todos)

    elif user_input.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index} - {item}')

    elif user_input.startswith('update'):
        try:
            index = int(user_input[7:])

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Invalid input.")
            continue

    elif user_input.startswith('complete'):
        try:
            index = int(user_input[9:])
            todos = get_todos()

            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove.strip()} has been completed!"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_input.startswith('exit'):
        break
    else:
        print("Invalid input")
print('Bye')
