from time import sleep

WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20


class Pomodoro:
    @staticmethod
    def countdown(minutes: int, label: str, badge: str):
        total_seconds = minutes * 60
        print(f"{badge} {minutes} minutes of {label} has started")

        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            print(f"⏱️ {mins:02}:{secs:02}   ", end="\r")

            sleep(1)
            total_seconds -= 1

        print("")
        print("\a")

    @staticmethod
    def run_pomodoro_set(count):
        for pomodoro_round in range(1, count + 1):
            print(f"\n🍅 Pomodoro set {pomodoro_round} of {count}")
            Pomodoro.countdown(WORK_MINUTES, "work", "👨🏻‍💻")

            if pomodoro_round % 4 == 0:
                Pomodoro.countdown(LONG_BREAK_MINUTES, "break", "💤")
            else:
                Pomodoro.countdown(SHORT_BREAK_MINUTES, "break", "☕")
