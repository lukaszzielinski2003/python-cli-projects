messages = {
    """
    Display an messages in red colors.
    """
    "invalid": "\033[91mInvalid number, try again\033[0m\n",
    "wrong_choice": "\033[91mWrong number, please try again\033[0m\n",
    "interrupt": "\033[91mProgram interrupted\033[0m\n",
    "exit": "\033[93mGoodbye!\033[0m",
}


def menu() -> None:
    """
    Print the ToDoList menu with available operations.
    """
    print("=" * 14)
    print("|  ToDoList  |")
    print("=" * 14)
    print("| 1. Show    |")
    print("| 2. Add     |")
    print("| 3. Delete  |")
    print("| 4. Exit    |")
    print("=" * 14)
