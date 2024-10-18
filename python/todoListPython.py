tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    try:
        tasks.remove(task)
    except ValueError:
        print(f'Task "{task}" not found. Please try again.')

while True:
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
