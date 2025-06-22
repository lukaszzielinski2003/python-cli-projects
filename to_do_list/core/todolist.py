import json  # Used for saving and loading tasks in JSON format.


class ToDoList:
    def __init__(self, filename="tasks.json"):
        """
        Initializes a ToDoList instance with an empty task list and sets the filename for storage.
        """

        self.tasks = []
        self.FILE = filename

    def save_tasks(self):
        """
        Saves the current list of tasks to the JSON file specified by self.FILE.
        """
        with open(self.FILE, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        """
        Loads tasks from the JSON file; if the file does not exist or is invalid,
        initializes with an empty task list.
        """
        try:
            with open(self.FILE, "r") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def show(self):
        """
        Displays all tasks with their numbers, or notifies if the list is empty.
        """
        if not self.tasks:
            print("\033[91mYour list is empty\033[0m\n")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add(self):
        """
        Prompts the user to enter a new task, adds it to the list if not empty,
        saves the updated list, and provides feedback.
        """
        try:
            task = str(input("Enter your task: ")).strip()
            if task:
                self.tasks.append(task)
                self.save_tasks()
                print("\033[92mTask added successfully\033[0m\n")
            else:
                print("\033[91mEmpty task is not allowed\033[0m\n")
        except ValueError:
            print("\033[91mInvalid task, try again\033[0m\n")

    def remove(self):
        """
        Shows the list of tasks, prompts the user to select a task number to remove,
        deletes the selected task if valid, saves changes, and provides feedback.
        """
        self.show()
        try:
            number = int(input("Enter the number of task: "))
            if 1 <= number <= len(self.tasks):
                self.tasks.pop(number - 1)
                self.save_tasks()
                print("\033[92mTask removed successfully\033[0m\n")
        except ValueError:
            print("\033[91mInvalid number, try again\033[0m\n")
