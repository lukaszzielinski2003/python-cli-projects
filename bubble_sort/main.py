"""
CLI entry point for performing bubble sort.

Allows the user to choose ascending or descending order
and input a list of numbers to be sorted using the Bubble Sort algorithm.
"""

from core.logic import bubble_sort_asc, bubble_sort_desc
from cli.interface import menu, handle_user_input, message


def main():
    """
    Run the CLI interface for Bubble Sort.

    Displays a menu to choose sorting order, handles user input,
    and calls the appropriate sorting function.

    Gracefully handles invalid input and keyboard interrupts.
    """
    try:
        operations = {1: bubble_sort_asc, 2: bubble_sort_desc}
        while True:
            menu()
            try:
                choice = int(input("Select option: "))
                if choice == 3:
                    message("exit")
                    break
                elif choice not in operations:
                    message("not_operation")
                else:
                    nums = handle_user_input()
                    if nums:
                        operations[choice](nums)
                print()
            except ValueError:
                message("not_operation")
    except KeyboardInterrupt:
        message("ctrl_c")


if __name__ == "__main__":
    main()
