import random


def get_user_choice() -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "()?!@#$"

    chars = ""

    if input("Include lowercase letters? (y/n): ").lower() == "y":
        chars += lowercase
    if input("Include uppercase letters? (y/n): ").lower() == "y":
        chars += uppercase
    if input("Include digits? (y/n): ").lower() == "y":
        chars += digits
    if input("Include special characters? (y/n): ").lower() == "y":
        chars += specials

    if not chars:
        print("\033[91mYou must select at least one character type!\033[0m\n")
    return chars


def generate_password(chars: str) -> str:
    if not chars:
        return ""

    try:
        length = int(input("Enter number of characters: "))
        if length <= 0:
            print("\033[91mThe length must be greater than 0\033[0m")
            return ""
    except ValueError:
        print("\033[91mPlease enter the number\n\033[0m")
        return ""
    return "".join(random.choice(chars) for _ in range(length))
