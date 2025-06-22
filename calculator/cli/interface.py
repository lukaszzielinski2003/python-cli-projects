def error() -> None:
    """
    Display an error message in red color.
    """
    print("\033[91mError, please try again\033[0m")


def show_result(result: float) -> None:
    """
    Display the calculation result in green color, rounded to 3 decimals.
    """
    print(f"\033[92mResult: {round(result, 3)}\033[0m")


def menu() -> None:
    """
    Print the calculator menu with available operations.
    """
    print("=" * 18)
    print("| CLI CALCULATOR |")
    print("=" * 18)
    print("| 1. Add         |")
    print("| 2. Subtract    |")
    print("| 3. Multiply    |")
    print("| 4. Divide      |")
    print("| 5. Power       |")
    print("| 6. Exit        |")
    print("=" * 18)
