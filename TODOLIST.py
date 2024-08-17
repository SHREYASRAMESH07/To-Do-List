import json
import os

# File to store the tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks):
            status = 'Done' if task['completed'] else 'Not Done'
            print(f"{idx + 1}. {task['title']} - {status}")

# Add a task
def add_task(tasks, title):
    tasks.append({'title': title, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{title}' added.")

# Complete a task
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['title']}' marked as complete.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter the task title: ")
            add_task(tasks, title)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
