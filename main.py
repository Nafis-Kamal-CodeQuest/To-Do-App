import time
import functions

time = time.strftime("%b %d,%Y %M:%H:%S")
print(time)

while True:
    todos = []

    print("-----Welcome To Task Manager-----")
    print("1. Add Task")
    print("2. View Task")
    print("3. Edit Task")
    print("4. Delete Tasks")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Write the task : ")
        task = input()
        functions.add_todo(task)
        print("Task Added")
    elif choice == "2":
        functions.show_todo()

    elif choice == "3":
        functions.edit_todo()
    elif choice == "4":
        functions.delete_todo()
    elif choice == "5":
        break
