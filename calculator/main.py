"""
CLI Calculator main program module.
"""

from core.calculator import Calculator
from cli.interface import menu, error, show_result


def main() -> None:
    """
    Main function to run the CLI calculator program.

    Show the menu, get user input, perform calculations using Calculator,
    display results, handle errors, and allow exiting the program.
    """
    operations = {
        1: Calculator.add,
        2: Calculator.subtract,
        3: Calculator.multiply,
        4: Calculator.divide,
        5: Calculator.power,
    }

    try:
        while True:
            menu()

            try:
                choice = int(input("Select operation: "))
            except ValueError:
                error()
                continue

            if choice == 6:
                print("Goodbye!")
                break

            if choice in operations:
                try:
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))

                    result = operations[choice](a, b)
                    show_result(result)

                except ValueError:
                    error()
                except ZeroDivisionError:
                    print("\033[91mYou can't divide by zero!\033[0m")
            else:
                error()

    except KeyboardInterrupt:
        print("\n\033[91mProgram interrupted. Goodbye!\033[0m")


if __name__ == "__main__":
    main()
