![DEMO GUI](https://i.imgur.com/WtaYBkJ.gif)
![DEMO WEB](https://i.imgur.com/wUhgaK8.gif)

Live [Demo](https://phucleit96-cloud-to-do-web-aludv7.streamlit.app/)

# GUI Todo Application

This repository contains a Python script for a GUI Todo application.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate into the cloned repository:
    ```
    cd yourrepository
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the script:
    ```
    python gui.py
    ```

## Usage

This application allows you to manage your todos. You can add, edit, and complete tasks. To add a task, enter the task in the input box and click 'Add'. To edit a task, select the task from the list, modify it in the input box, and click 'Edit'. To complete a task, select the task from the list and click 'Complete'.

## Code Explanation

This Python script uses the PySimpleGUI library to create a GUI for a Todo application. The script handles different events triggered by user interactions with the GUI.

### Add Event

When the "Add" button is clicked, the application performs the following steps:

1. Retrieves the current list of todos.
2. Appends the new todo entered by the user.
3. Writes the updated list back to the file.
4. Updates the list displayed in the GUI.

### Edit Event

When the "Edit" button is clicked, the application performs the following steps:

1. Tries to get the currently selected todo.
2. If a todo is selected, it replaces the selected todo with the new todo entered by the user.
3. Writes the updated list back to the file.
4. Updates the list displayed in the GUI.
5. If no todo is selected, it shows a popup message asking the user to select a todo.

### Complete Event

When the "Complete" button is clicked, the application performs the following steps:

1. Tries to get the currently selected todo.
2. If a todo is selected, it removes the selected todo from the list.
3. Writes the updated list back to the file.
4. Updates the list displayed in the GUI.
5. If no todo is selected, it shows a popup message asking the user to select a todo.

### Todo Selection Event

When a todo is selected from the list, the application updates the input box with the content of the selected todo.

At the end of the script, the window is closed with `window.close()`.


# Web Todo Application

This repository also contains a Python script for a Web Todo application using Streamlit.

## Usage

This web application allows you to manage your todos. You can add and complete tasks. To add a task, enter the task in the text input box and press enter. To complete a task, check the checkbox next to the task.

## Code Explanation

This Python script uses the Streamlit library to create a web interface for a Todo application. The script handles different events triggered by user interactions with the web interface.

### Add Event

When a new todo is entered in the text input box, the application performs the following steps:

1. Retrieves the new todo entered by the user.
2. Appends the new todo to the list.
3. Writes the updated list back to the file.

### Complete Event

When the checkbox next to a todo is checked, the application performs the following steps:

1. Removes the selected todo from the list.
2. Writes the updated list back to the file.
3. Reruns the app to update the display.

At the end of the script, the application continuously waits for user input with `st.rerun()`.

