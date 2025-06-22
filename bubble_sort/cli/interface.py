def menu() -> None:
    """
    Display main menu
    """
    print("+=====================================+")
    print("|           CLI Bubble Sort           |")
    print("+-------------------------------------+")
    print("|   This example covers only numbers  |")
    print("+-------------------------------------+")
    print("|        Available operations:        |")
    print("+=====================================+")
    print("| 1. Ascending order                  |")
    print("+-------------------------------------+")
    print("| 2. Descending order                 |")
    print("+-------------------------------------+")
    print("| 3. Exit program or Ctrl + c         |")
    print("+=====================================+")


def handle_user_input() -> list:
    """
    Converts user's input into list
    """
    try:
        user = input("Enter numbers (add 'space' after each number): ")
        nums = list(map(int, user.split()))
        if not nums:
            message("empty_input")
        return nums
    except ValueError:
        message("invalid_input")
        return []


def message(msg_type: str) -> None:
    """
    Display standardized error or info messages based on the type.
    """
    messages = {
        "exit": "Goodbye",
        "ctrl_c": "Program interrupted",
        "not_operation": "Invalid option. Please select a valid operation.",
        "select": "Please select operation",
        "invalid_input": "Please enter numbers",
        "empty_input": "No numbers entered",
    }
    print(messages.get(msg_type, "Unknown message type"))
