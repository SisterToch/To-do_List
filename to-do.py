#!/usr/bin/python3

import tkinter as tk
import pickle """this module helps save and load tasks to and from a file"""

def add_task(): """appears everytime i click add task button"""
    task = task_entry.get() """get the task from task_entry and save in task"""
    if task: """checks if task is empty"""
        tasks.append(task) """append to tasks"""
        update_task_list() """to refresh the tasklist"""
        task_entry.delete(0, tk.End) """delete all the text from 0 to end of text"""
        save_tasks()

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks[index]
        update_task_list()
        save_tasks()
