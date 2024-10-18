import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def mark_completed():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        listbox.delete(selected_task)
        completed_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons for adding, marking as completed, and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

add_button.pack(pady=5)
mark_button.pack(pady=5)
remove_button.pack(pady=5)

# Lists for displaying tasks and completed tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)

listbox.pack(pady=10)
completed_listbox.pack(pady=10)

# Run the application
root.mainloop()

