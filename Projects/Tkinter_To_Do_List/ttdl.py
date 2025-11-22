# 📜 To-Do List GUI App
# By Kaushik 🚀

import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "todo.txt"

# 🧾 Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert(tk.END, task)

# 💾 Save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# ➕ Add task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("⚠️ Warning", "Please enter a task!")

# ❌ Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("⚠️ Warning", "Please select a task to delete!")

# 🧹 Clear all tasks
def clear_all():
    if messagebox.askyesno("🧹 Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

# 🪟 Create GUI window
root = tk.Tk()
root.title("📜 To-Do List by Kaushik")
root.geometry("400x500")
root.config(bg="#222831")

# 🏷️ Title Label
title = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 18, "bold"), bg="#222831", fg="#FFD369")
title.pack(pady=10)

# 🖊️ Input Entry
entry_frame = tk.Frame(root, bg="#222831")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=22, bd=2)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(entry_frame, text="➕ Add", command=add_task, bg="#FFD369", font=("Helvetica", 12, "bold"))
add_btn.pack(side=tk.LEFT)

# 📋 Listbox for tasks
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    listbox_frame,
    font=("Helvetica", 14),
    width=30,
    height=15,
    yscrollcommand=scrollbar.set,
    selectbackground="#FFD369",
    bg="#393E46",
    fg="white"
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# 🔘 Buttons for actions
btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack(pady=15)

delete_btn = tk.Button(btn_frame, text="❌ Delete", command=delete_task, bg="#FF6B6B", font=("Helvetica", 12, "bold"))
delete_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(btn_frame, text="🧹 Clear All", command=clear_all, bg="#00ADB5", font=("Helvetica", 12, "bold"))
clear_btn.pack(side=tk.LEFT, padx=10)

# 🚀 Load existing tasks
load_tasks()

root.mainloop()
