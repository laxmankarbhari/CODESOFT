import tkinter as tk
from tkinter import messagebox
import os

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        if not task.startswith("✔ "):  
            task_listbox.delete(selected)
            task_listbox.insert(tk.END, f"✔ {task}")
            save_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    if task_listbox.size() > 0:
        task_listbox.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "No tasks to clear!")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

load_tasks()

root.mainloop()
