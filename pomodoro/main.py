from cli.interface import Interface
from core.logic import Pomodoro
from time import sleep


def main():
    try:
        while True:
            Interface.clear_terminal()
            Interface.show_info()
            sleep(5)

            Interface.refresh_screen()
            count = Interface.handle_user_input()

            Interface.refresh_screen()
            Pomodoro.run_pomodoro_set(count)

    except KeyboardInterrupt:
        print("\n👋 Program terminated by user. Goodbye!")


if __name__ == "__main__":
    main()
