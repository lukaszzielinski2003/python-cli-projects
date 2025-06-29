import os


class Interface:
    @staticmethod
    def show_banner() -> None:
        print("+" + "-" * 38 + "+")
        print(f"|   {'🍅 Pomodoro Timer 🍅':^30}   |")
        print("+" + "-" * 38 + "+")
        print("| To exit the program press 'Ctrl + C' |")
        print("+" + "-" * 38 + "+")

    @staticmethod
    def clear_terminal() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def show_info() -> None:
        print(
            "The 🍅 Pomodoro Technique 🍅 is a time management method that helps you stay focused and productive."
        )
        print(
            "It consists of working in four 25-minute sessions, called Pomodoros, each followed by a 5-minute short break."
        )
        print(
            "After completing four Pomodoros, you take a longer break of around 20 minutes to rest and recharge"
        )

    @staticmethod
    def handle_user_input() -> int:
        while True:
            user_input = input(
                "How many Pomodoro sets would you like to do? (or 'q' to quit): "
            )
            if user_input.lower() in ("q", "quit", "exit"):
                print("Exiting program. Goodbye!")
                exit(0)
            try:
                count = int(user_input)
                if count > 0:
                    return count
                else:
                    print("⚠️ Please enter a valid number (1 or higher).")
            except ValueError:
                print("⚠️ Please enter a number (1 or higher).")

    @staticmethod
    def refresh_screen():
        Interface.clear_terminal()
        Interface.show_banner()
