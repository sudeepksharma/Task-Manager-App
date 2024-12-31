# Task Management App

## Introduction
Welcome to the Task Management App! This simple Python application helps you manage your daily tasks efficiently. You can add, update, delete, and view tasks seamlessly.

## Features
- Add tasks
- Update tasks
- Delete tasks
- View tasks

## How to Use
1. Run the script.
2. Enter the total number of tasks you want to add initially.
3. Follow the on-screen instructions to manage your tasks.

## Code Explanation
The `task()` function performs the following operations:
1. Initializes an empty list to store tasks.
2. Prompts the user to enter the total number of initial tasks.
3. Provides a menu to add, update, delete, and view tasks.




## Example
def task(): tasks = [] print("----- Welcome to the Task Management App -----")

total_task = int(input("Enter the total number of tasks you want to add: ")) for i in range(total_task): task_name = input(f"Enter the task {i}: ") tasks.append(task_name)

print(f"Today's tasks are: \n {tasks}")

while True: 
operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
if operation == 1: 
add = input("Enter task you want to add: ")
tasks.append(add) 
print(f"Task {add} has been added to the list: {tasks}")
elif operation == 2: 
update = input("Enter task you want to update: ") 
update_index = tasks.index(update) new_task = input("Enter the new task: ") 
tasks[update_index] = new_task 
print(f"Task {update} has been updated to the list: {tasks}") 
elif operation == 3: 
delete = input("Enter task you want to delete: ") 
tasks.remove(delete) 
print(f"Task {delete} has been deleted from the list: {tasks}") 
elif operation == 4: 
print(f"Today's tasks are: \n {tasks}") 
elif operation == 5: 
break else: 
print("Invalid Input: Please enter a valid input from 1-5")