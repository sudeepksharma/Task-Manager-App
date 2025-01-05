# To Do List App

A simple Task Manager App built with Python and Tkinter that allows you to manage your tasks efficiently. The app supports adding, deleting, editing, marking tasks as completed, saving and loading tasks from a file, toggling dark mode, and adding tasks using voice input.

## Features

- Add a new task
- Delete a task
- Edit a task
- Mark a task as completed
- Save tasks to a file
- Load tasks from a file
- Clear all tasks
- Toggle dark mode
- Add task using voice input

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `speech_recognition` library
- `pyaudio` library (for voice input)

## Installation

1. Clone the repository or download the source code.
2. Install the required libraries using pip:
    ```sh
    pip install speechrecognition pyaudio
    ```
3. Run the `app.py` file:
    ```sh
    python app.py
    ```

## Usage

1. **Add Task**: Enter a task in the entry field and click "Add Task".
2. **Delete Task**: Select a task from the list and click "Delete Task".
3. **Edit Task**: Select a task from the list, enter the new task in the entry field, and click "Edit Task".
4. **Mark Completed**: Select a task from the list and click "Mark Completed".
5. **Save Tasks**: Click "Save Tasks" to save the current tasks to a file.
6. **Load Tasks**: Click "Load Tasks" to load tasks from a file.
7. **Clear Tasks**: Click "Clear Tasks" to clear all tasks from the list.
8. **Toggle Dark Mode**: Click "Toggle Dark Mode" to switch between light and dark mode.
9. **Add Task by Voice**: Click "Add Task by Voice" and speak the task to add it using voice input.

## File Structure

- [app.py](http://_vscodecontentref_/0): The main application file.
- [tasks.json](http://_vscodecontentref_/1): The file where tasks are saved (created automatically).

## License

This project is licensed under the MIT License.
