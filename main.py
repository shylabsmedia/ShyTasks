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

def choose_priority():

    while True:
        print("\nChoose task priority:")
        print("1 - Low")
        print("2 - Medium")
        print("3 - High")
        print("4 - Urgent")

        choice = input("Enter your choice: ")

        if choice == "1":
            return "Low"

        elif choice == "2":
            return "Medium"

        elif choice == "3":
            return "High"

        elif choice == "4":
            return "Urgent"

        print("Invalid choice. Please try again.")

def choose_category():

    while True:
        print("\nChoose task category:")
        print("1 - Personal")
        print("2 - Work")
        print("3 - Study")
        print("4 - Shopping")
        print("5 - Home")
        print("6 - Other")

        choice = input("Enter your choice: ")

        if choice == "1":
            return "Personal"

        elif choice == "2":
            return "Work"

        elif choice == "3":
            return "Study"

        elif choice == "4":
            return "Shopping"

        elif choice == "5":
                return "Home"

        elif choice == "6":
            return "Other"

        print("Invalid choice. Please try again.")

def add_task(manager):

    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    priority = choose_priority()
    category = choose_category()
    due_date = input("Enter task due date (DD-MM-YYYY): ")

    task = manager.add_task(title, description, priority, category, due_date)
    print(f"Task '{task.title}' added successfully with ID {task.id}!")
    input("\nPress Enter to continue...")

def view_tasks(manager):

    tasks = manager.view_tasks()

    if not tasks:
        print("No tasks available.")
        input("\nPress Enter to continue...")
        return

    print("\n========== TASK LIST ==========")
    for task in tasks:
        print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Category: {task.category}, Due Date: {task.due_date}, Status: {task.status}")
    print("===============================")
    input("\nPress Enter to continue...")

def delete_task(manager):

    tasks = manager.view_tasks()

    if not tasks:
        print("\nNo tasks available.")
        input("\nPress Enter to continue...")
        return

    while True:
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    task = manager.delete_task(task_id)

    if task:
        print(f"\nTask '{task.title}' deleted successfully!")
    else:
        print("\nTask not found.")

    input("\nPress Enter to continue...")

while running:

    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(manager)
        
    elif choice == "2":
        view_tasks(manager)

    elif choice == "3":
        delete_task(manager)

    elif choice == "0":
        running = False
        print("Exiting ShyTasks. Goodbye!")

    else:
        print("Invalid choice. Please try again.")

    