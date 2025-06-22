def menu() -> None:
    """
    Display the main menu with available unit conversions.
    """
    print("+----------------+")
    print("| Unit Converter |")
    print("+----------------+")
    print("| 1. Km to Miles |")
    print("| 2. Miles to Km |")
    print("| 3. Kg to Lbs   |")
    print("| 4. Lbs to Kg   |")
    print("| 5. Exit        |")
    print("+----------------+")


def error_msg(msg_type: str) -> None:
    """
    Display standardized error or info messages based on the type.
    """
    messages = {
        "value": "Wrong number, please try again",
        "ctrl_c": "Program interrupted...",
        "exit": "Goodbye!",
        "unknown": "Unknown operation, please try again",
        "select": "Please select operation",
    }
    print(messages.get(msg_type, "Unknown error"))
