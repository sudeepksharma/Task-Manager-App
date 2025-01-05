import tkinter as tk
from tkinter import messagebox
import json
import os
import speech_recognition as sr

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to edit a task
def edit_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        new_task = entry_task.get()
        if new_task != "":
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Function to save tasks to a file
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    messagebox.showinfo("Save Success", "Tasks saved successfully.")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            listbox_tasks.delete(0, tk.END)
            for task in tasks:
                listbox_tasks.insert(tk.END, task)
    else:
        messagebox.showwarning("Load Error", "No saved tasks found.")

# Function to toggle dark mode
def toggle_dark_mode():
    if root.cget('bg') == 'white':
        root.configure(bg='black')
        for widget in root.winfo_children():
            widget.configure(bg='black', fg='white')
    else:
        root.configure(bg='white')
        for widget in root.winfo_children():
            widget.configure(bg='white', fg='black')

# Function to add task using voice input
def add_task_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for task...")
        audio = recognizer.listen(source)
        try:
            task = recognizer.recognize_google(audio)
            listbox_tasks.insert(tk.END, task)
            messagebox.showinfo("Voice Input", f"Task added: {task}")
        except sr.UnknownValueError:
            messagebox.showwarning("Voice Input Error", "Could not understand the audio.")
        except sr.RequestError as e:
            messagebox.showwarning("Voice Input Error", f"Could not request results; {e}")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.configure(bg='white')

# Create the UI elements
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_mark_completed = tk.Button(root, text="Mark Completed", width=48, command=mark_completed)
button_mark_completed.pack()

button_edit_task = tk.Button(root, text="Edit Task", width=48, command=edit_task)
button_edit_task.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tk.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_dark_mode = tk.Button(root, text="Toggle Dark Mode", width=48, command=toggle_dark_mode)
button_dark_mode.pack()

button_voice_input = tk.Button(root, text="Add Task by Voice", width=48, command=add_task_voice)
button_voice_input.pack()

# Load tasks from file when the app starts
load_tasks()

# Run the main loop
root.mainloop()
