# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()


    # match user_action:
    if user_action.startswith('add' or 'new'):
        todo = user_action[4:].replace('\n','').strip()

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos,"todos.txt")

    elif 'show' in user_action:

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:

            # number = int(input("Enter the number of todo you want to edit: "))
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("enter the new todo: ").replace('\n','').strip()
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except (ValueError, IndexError):
            print("Invalid input or index out of range.")

    elif user_action.startswith('complete'):
        try:
            # number = int(input("Number of todo to complete: "))
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Hey this is the wrong command, please retype one")
print("See ya")


