


def read_files():
    with open('todos.txt','r') as file:
        todos = file.readlines()
        return todos

def write_files(todos):
    with open('todos.txt','w') as file:
        file.writelines(todos)

def add_todo(user_input):
    task = user_input.strip()
    todos = read_files()
    todos.append(task + '\n')
    write_files(todos)

def show_todo():
    todos = read_files()
    if(len(todos) == 0):
        print("No To Do found")
        return
    else:
        for index,item in enumerate(todos,1):
            item = item.strip('\n')
            row = f"{index} -  {item}"
            print(row)

def edit_todo():
    todos = read_files()
    if len(todos) == 0:
        print("No To do found")
        return
    else:
        show_todo()

        to_edit_index = int(input("Which todo you want to edit?")) -1
        new_task = input("Write new task: ")
        todos[to_edit_index] = new_task + '\n'
        write_files(todos)
        print("Task Updated")



def delete_todo():
    todos = read_files()
    if len(todos) == 0:
        print("No To do found")
        return
    else:
        to_delete = int(input("Which to do you want to delete?"))
        todos.pop(to_delete)
        write_files(todos)
        print("ToDo Deleted")

