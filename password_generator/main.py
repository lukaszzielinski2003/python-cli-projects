from cli.interface import menu
from core.logic import get_user_choice, generate_password


def main():
    while True:
        menu()
        try:
            choice = int(input("Select operation: "))
        except ValueError:
            print("\033[91mError, please enter number\033[0m\n")
            continue

        if choice == 2:
            print("Goodbye!")
            break
        elif choice == 1:
            chars = get_user_choice()
            password = generate_password(chars)
            if password:
                print(f"Your password: \033[92m{password}\033[0m\n")
        else:
            print("\033[91mPlease select correct operation\033[0m\n")
            continue


if __name__ == "__main__":
    main()
