#!/usr/bin/python3


"""this is where i import module, and here, i am importing pickle"""
import pickle


"""Now the functions, follow the thought process"""
def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
            tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        return pickle.dump(tasks, f)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def remove_task(tasks, index):
    del tasks[index]
    save_tasks(tasks)

