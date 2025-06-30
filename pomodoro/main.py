from cli.interface import Interface
from core.logic import Pomodoro
from time import sleep


def main():
    """
    Starts the Pomodoro CLI application loop.

    Displays an introduction, prompts the user for the number of Pomodoro sets,
    and runs the timer with appropriate breaks. Handles exit gracefully.
    """
    try:
        while True:
            Interface.clear_terminal()
            Interface.show_info()
            sleep(5)  # Allows time for the user to read the Pomodoro explanation.

            Interface.refresh_screen()
            count = Interface.handle_user_input()

            Interface.refresh_screen()
            Pomodoro.run_pomodoro_set(count)

    except KeyboardInterrupt:
        print("\n👋 Program terminated by user. Goodbye!")


if __name__ == "__main__":
    main()
