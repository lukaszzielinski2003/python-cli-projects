# 🍅 CLI Pomodoro Timer

A simple and interactive **command-line Pomodoro timer** to help you stay focused and productive using the Pomodoro Technique.

---

## ✨ Features

- Works in Pomodoro sets of 25-minute work sessions
- Short breaks of 5 minutes after each work session
- Long break of 20 minutes after every 4 Pomodoros
- Clear and user-friendly CLI interface
- Input validation and ability to quit anytime (`q` or `Ctrl + C`)
- Cross-platform terminal clear support

---

## 🛠️ How to Run

1. Clone the repo or download the files.
2. Make sure you have **Python 3.10+** installed.
3. Run the program:

```bash
python main.py
```

---

## 🕹️ Usage

1. After starting, read the brief introduction about the Pomodoro Technique.

2. Enter how many Pomodoro sets you want to do (or type q to quit).

3. The timer will count down your work sessions and breaks automatically.

4. After every 4 work sessions, you will get a longer break.

5. Use Ctrl + C anytime to exit the program.

---

## 🧪 Sample Output

```text
+--------------------------------------+
|         🍅 Pomodoro Timer 🍅         |
+--------------------------------------+
| To exit the program press 'Ctrl + C' |
+--------------------------------------+

The 🍅 Pomodoro Technique 🍅 is a time management method that helps you stay focused and productive.
It consists of working in four 25-minute sessions, called Pomodoros, each followed by a 5-minute short break.
After completing four Pomodoros, you take a longer break of around 20 minutes to rest and recharge.

How many Pomodoro sets would you like to do? (or 'q' to quit): 4

🍅 Pomodoro set 1 of 4
👨🏻‍💻 25 minutes of work has started
⏱️ 24:59
...
☕ 5 minutes of break has started
⏱️ 04:59
...

🍅 Pomodoro set 4 of 4
👨🏻‍💻 25 minutes of work has started
⏱️ 24:59
...
💤 20 minutes of break has started
⏱️ 19:59
...
Program terminated by user. Goodbye!
```

---

## 🧾 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
