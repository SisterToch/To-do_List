import tkinter as tk
import tkinter.ttk as ttk
from logic_pickle import load_tasks, save_tasks, add_task, remove_task
"""we have imported the important files for incorporating the gui"""


def add_task_gui():
    """functions for the add button"""
    task = task_entry.get()
    if task:
        add_task(tasks, task)
        update_task_list()
        task_entry.delete(0, tk.END)

def remove_task_gui():
    """to remove the selected task"""
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        remove_task(tasks, index)
        update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

"""load your tasks from the file"""
tasks = load_tasks()

"""the application window"""
window = tk.Tk()

"""give your window a title"""
window.title("MY To Do List")

"""now to your widgets"""
"""let us do the label."""
task_label = tk.Label(window, text="Welcome! What tasks do you want to do?")
task_label.pack(pady=5)

task_entry = tk.Entry(window, width=60)
task_entry.pack(pady=5)

task_button = tk.Button(window, text="Add New Task!", command=add_task_gui)
task_button.pack(pady=5)

task_button = tk.Button(window, text="Delete Task", command=remove_task_gui)
task_button.pack(pady=5)

"""the table like interface"""
task_listbox = ttk.Treeview(window, columns=("Task #", "Task", "Comment", "Due Date", "Completed"), show="headings")
task_listbox.heading("Task #", text="Task #")
task_listbox.heading("Task", text="Task")
task_listbox.heading("Comment", text="Comment")
task_listbox.heading("Due Date", text="Due Date")
task_listbox.heading("Completed", text="Completed")
task_listbox.pack(pady=17)

style = ttk.Style()
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

update_task_list
window.mainloop()
