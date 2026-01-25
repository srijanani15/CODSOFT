# To-Do List Application using Python

def display_menu():
    print("\nTO-DO LIST MENU")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

tasks = []

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    # Add a task
    if choice == "1":
        task_name = input("Enter the task: ")
        tasks.append({"task": task_name, "status": "Pending"})
        print(f"Task '{task_name}' added successfully.")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['task']} - {task['status']}")

    # Mark task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                task_name = tasks[task_no - 1]["task"]
                tasks[task_no - 1]["status"] = "Completed"
                print(f"Task '{task_name}' has been marked as completed.")
            else:
                print("Invalid task number.")

    # Delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted_task = tasks.pop(task_no - 1)
                print(f"Task '{deleted_task['task']}' has been deleted.")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Exiting the application.")
        break

    else:
        print("Please enter a valid option.")

