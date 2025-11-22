# 📜 To-Do List App
# By Kaushik 🚀

import os
import time

FILENAME = "todo.txt"

def show_tasks():
    print("\n🗒️ Your Tasks:")
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("👉 No tasks yet. Add one!")
        return
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(f"✅ Task added: {task}")

def delete_task(task_no):
    if not os.path.exists(FILENAME):
        print("⚠️ No tasks to delete!")
        return
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    if 0 < task_no <= len(tasks):
        removed = tasks.pop(task_no - 1)
        with open(FILENAME, "w") as file:
            file.writelines(tasks)
        print(f"🗑️ Task removed: {removed.strip()}")
    else:
        print("⚠️ Invalid task number!")

def clear_all():
    open(FILENAME, "w").close()
    print("🧹 All tasks cleared!")

def main():
    while True:
        print("\n📋 To-Do Menu")
        print("1️⃣ Show tasks")
        print("2️⃣ Add task")
        print("3️⃣ Delete task")
        print("4️⃣ Clear all")
        print("5️⃣ Exit")

        choice = input("👉 Choose (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("✏️ Enter new task: ")
            add_task(task)
        elif choice == '3':
            show_tasks()
            try:
                num = int(input("❌ Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == '4':
            clear_all()
        elif choice == '5':
            print("👋 Goodbye, keep hustling!")
            break
        else:
            print("⚠️ Invalid choice!")

        time.sleep(1)

if __name__ == "__main__":
    main()
