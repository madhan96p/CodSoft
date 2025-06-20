import json
import os

FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({'title': title, 'done': False})
    print("Task added.")

def mark_done(tasks):
    show_tasks(tasks)
    idx = int(input("Mark task number as done: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['done'] = True
        print("Marked as done.")

def delete_task(tasks):
    show_tasks(tasks)
    idx = int(input("Delete task number: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"Removed: {removed['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Saved & Exited. Bye! 👋")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
