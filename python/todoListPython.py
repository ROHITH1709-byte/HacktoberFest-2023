tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    try:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully.')
    except ValueError:
        print(f'Task "{task}" not found in the list.')

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
        print(f'Task "{task}" added successfully.')
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
