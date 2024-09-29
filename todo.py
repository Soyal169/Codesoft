import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Task list to store the tasks
tasks = []

# Function to update the listbox with the current tasks
def update_listbox():
    listbox.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a new task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        task_index = listbox.curselection()[0]
        del tasks[task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to update a selected task
def update_task():
    try:
        task_index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            tasks[task_index] = new_task
            update_listbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a new task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Function to exit the application
def exit_app():
    root.quit()

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a listbox to display the tasks
listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Arial", 12),
    selectbackground="#a6a6a6",
    activestyle="none",
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Attach the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an entry box to enter new tasks
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=34,
    bd=2,
)
entry.pack(pady=20)

# Create buttons for adding, updating, deleting, and exiting
add_button = tk.Button(root, text="Add Task", width=16, command=add_task)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=16, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=16, command=delete_task)
delete_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=16, command=exit_app)
exit_button.pack(pady=20)

# Run the application
root.mainloop()
