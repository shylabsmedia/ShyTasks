from services.task_manager import TaskManager

manager = TaskManager()

running = True

def show_menu():
    print("\n========== SHYTASKS ==========")
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Delete Task")
    print("0 - Exit")
    print("===============================")

def add_task(manager):
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    priority = input("Enter task priority (Low, Medium, High): ")
    category = input("Enter task category: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")

    task = manager.add_task(title, description, priority, category, due_date)
    print(f"Task '{task.title}' added successfully with ID {task.id}!")

def view_tasks(manager):
    tasks = manager.view_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\n========== TASK LIST ==========")
    for task in tasks:
        print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Category: {task.category}, Due Date: {task.due_date}, Status: {task.status}")
    print("===============================")

def delete_task(manager, task_id):
    tasks = manager.view_tasks()
    task_to_delete = next((task for task in tasks if task.id == task_id), None)

    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task '{task_to_delete.title}' deleted successfully!")
    else:
        print(f"No task found with ID {task_id}.")

while running:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(manager)
        
    elif choice == "2":
        view_tasks(manager)

    elif choice == "3":
        task_id = int(input("Enter the ID of the task to delete: "))
        delete_task(manager, task_id)

    elif choice == "0":
        running = False
        print("Exiting ShyTasks. Goodbye!")

    else:
        print("Invalid choice. Please try again.")

    