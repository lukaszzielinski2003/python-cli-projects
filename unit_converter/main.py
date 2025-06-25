"""
Main entry point for the CLI unit converter.

This module runs text-based interface allowing users to convert between:
 - kilograms and pounds.
 - kilometers and miles.
 - celsius and fahrenheit
"""

from cli.interface import menu, error_msg
from core.converter import Converter


def main() -> None:
    """
    Run the CLI unit converter.

    Displays a menu of conversion options and prompts the user for input.
    Handles user selection and invokes the appropriate conversion method from the Converter class.

    Handles invalid input and keyboard interrupts gracefully.
    """
    operations = {
        1: Converter.km_to_miles,
        2: Converter.miles_to_km,
        3: Converter.kg_to_lbs,
        4: Converter.lbs_to_kg,
        5: Converter.cel_to_far,
        6: Converter.far_to_cel
    }

    unit_labels = {1: "miles", 2: "kilometers", 3: "pounds", 4: "kilograms", 5:"fahrenheit", 6: "celsius"}
    input_labels = {1: "kilometers", 2: "miles", 3: "kilograms", 4: "pounds", 5: "celsius", 6: "fahrenheit"}

    try:
        while True:
            menu()
            try:
                choice = int(input("Select operation: "))
                match choice:
                    case 7:
                        error_msg("exit")
                        break
                    case 1 | 2 | 3 | 4 | 5| 6:
                        try:
                            x = float(
                                input(f"Enter the number in {input_labels[choice]}: ")
                            )
                            result = operations[choice](x)
                            print(f"Result: {result:.2f} {unit_labels[choice]}\n")
                        except ValueError:
                            error_msg("value")
                        continue
                    case _:
                        error_msg("unknown")
                        continue
            except ValueError:
                error_msg("select")
                continue

    except KeyboardInterrupt:
        error_msg("ctrl_c")


if __name__ == "__main__":
    main()
