from time import sleep  # Import sleep function to simulate countdowns.

# Pomodoro time settings (in minutes)
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20


class Pomodoro:
    """
    Core Pomodoro logic for managing work and break sessions.
    """
    @staticmethod
    def countdown(minutes: int, label: str, badge: str):
        """
        Counts down the time for a Pomodoro session.

        Args:
            minutes (int): Duration of the timer in minutes.
            label (str): A label for the session type ("work" or "break").
            badge (str): An emoji symbol representing the session.
        """
        total_seconds = minutes * 60
        print(f"{badge} {minutes} minutes of {label} has started")

        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            print(f"⏱️ {mins:02}:{secs:02}   ", end="\r")

            sleep(1)
            total_seconds -= 1

        print("")  # Move to a new line after countdown.
        print("\a")  # System bell sound (may not work in all terminals).

    @staticmethod
    def run_pomodoro_set(count: int):
        """
        Runs a full Pomodoro session consisting of work and break cycles.

        Args:
            count (int): Number of Pomodoro work sessions to complete.
        """
        for pomodoro_round in range(1, count + 1):
            print(f"\n🍅 Pomodoro set {pomodoro_round} of {count}")
            Pomodoro.countdown(WORK_MINUTES, "work", "👨🏻‍💻")

            if pomodoro_round % 4 == 0:
                Pomodoro.countdown(LONG_BREAK_MINUTES, "break", "💤")
            else:
                Pomodoro.countdown(SHORT_BREAK_MINUTES, "break", "☕")
