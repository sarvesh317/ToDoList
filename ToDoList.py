import json
from datetime import datetime

def load_tasks():
    try:
        with open('sarvesh tasks', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('sarvesh tasks', 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date = input("Enter due date YYYY-MM-DD: ")
    tasks.append({'name': task_name, 'priority': priority, 'due_date': due_date, 'completed': False})
    save_tasks(tasks)

def remove_task(tasks):
    task_index = int(input("Enter index of task to remove: "))
    del tasks[task_index]
    save_tasks(tasks)

def mark_completed(tasks):
    task_index = int(input("Enter index of task to mark as completed: "))
    tasks[task_index]['completed'] = True
    save_tasks(tasks)

def display_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
