# Simple console-based To-Do List

def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    print("\nCurrent Tasks:")
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Removed your task and Exiting app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
