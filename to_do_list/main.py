"""
CLI ToDoList main program module.
"""

from core.todolist import ToDoList
from cli.interface import menu, messages


def main():
    """
    Main function to run the CLI ToDoList program.

    Shows the to-do list options, collects input from the user, executes task-related operations
    (such as adding, deleting, and viewing tasks), manages errors, and allows exiting the program.
    """
    todo = ToDoList()
    todo.load_tasks()
    operations = {1: todo.show, 2: todo.add, 3: todo.remove}
    try:
        while True:
            menu()
            try:
                choice = int(input("Select operation: "))
                if choice == 4:
                    print(messages["exit"])
                    break
                elif choice not in operations:
                    print(messages["wrong_choice"])
                    continue
                else:
                    operations[choice]()
            except ValueError:
                print(messages["invalid"])
    except KeyboardInterrupt:
        print(messages["interrupt"])


if __name__ == "__main__":
    main()
