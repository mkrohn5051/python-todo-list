todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})

def complete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True

def delete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list.pop(task_index)

def view_tasks():
    for i, task in enumerate(todo_list):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        task_index = int(input("Enter the task number to complete: "))
        complete_task(task_index)
    elif choice == '3':
        task_index = int(input("Enter the task number to delete: "))
        delete_task(task_index)
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please select again.")
