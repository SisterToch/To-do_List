#!/usr/bin/python3

import tkinter as tk
import pickle
"""this module helps save and load tasks to and from a file"""

def add_task():
    """appears everytime i click add task button"""
    task = task_entry.get()
    """get the task from task_entry and save in task"""
    if task:
        """checks if task is empty"""
        tasks.append(task)
        """append to tasks"""
        update_task_list()
        """to refresh the tasklist"""
        task_entry.delete(0, tk.END)
        """delete all the text from 0 to end of text"""
        save_tasks()

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks[index]
        update_task_list()
        save_tasks()

def update_task_list():
    task_listbox.delete(0, tk.END)
    """this clears the existing tasks in the list box"""
    for task in tasks:
        task_listbox.insert(tk.END, task)
        """inserts the new task into the taskslistbox at the end of the list"""


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

try:
    with open('tasks.pkl', 'rb') as f:
        tasks = pickle.load(f)
except FileNotFoundError:
    tasks = []

"""create the application window"""
window = tk.Tk()
window.title("My To-Do List")

""" Create and configure widgets"""
task_label = tk.Label(window, text="Enter new task:")
"""creates a label widget('tk.Label') with the text "enter task"""
task_label.pack(pady=5)
"""places the task_label in the GUI,with vertical padding 5pixels below the label"""

task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

task_listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=10)
task_listbox.pack(pady=10)

update_task_list()

"""start the GUI loop"""
window.mainloop()
