from colorama import Fore
import json


def login(path: str = "auth.json") -> str:
    with open(path, "r") as f:
        list_of_users = json.loads(f.read())
    username = input(Fore.LIGHTYELLOW_EX + "Insert username: ")
    while username.lower() not in list_of_users:
        username = input(Fore.RED + "User not found! Try again: ")
    attempts = 3
    passwd = input(Fore.LIGHTYELLOW_EX + "Password: ")
    while list_of_users[username.lower()] != passwd:
        attempts -= 1
        passwd = input(Fore.RED + f"Wrong password. {attempts} attempts left. Try again: ")
        if attempts == 0:
            print(Fore.RED + "You exceeded the maximum number of attempts!")
            exit()

    return username


def login_menu():
    print(Fore.LIGHTBLUE_EX + f"{10 * '*' + ' '}Welcome to your budget app!{' ' + 10 * '*'}")
    login_page = Fore.GREEN + """
        1. Create new user
        2. Login with existing user
        3. Forgot password\n"""
    user_pick = input(login_page)

    match user_pick:
        case "1":
            add_user()
        case "2":
            user = login()
            logged_in_user_menu(user)
        case "3":
            pass


def add_user(path: str = "auth.json"):
    with open(path, "r") as f:
        list_of_users = json.loads(f.read())

    username = input("Choose your username: ")
    while username in list_of_users:
        username = input("Username taken. Please try another one:")
    passwd = " "
    confirm = "a"
    while passwd != confirm:
        passwd = input("Create password: ")
        confirm = input("Confirm password: ")
        if passwd != confirm:
            print("Passwords don't match! ")
        else:
            break
    new_user = {username: {"password": passwd, "balance": 0}}
    list_of_users.update(new_user)
    with open(path, "w") as f:
        f.write(json.dumps(list_of_users, indent=4))
    print("User added successfully!")


def print_balance(users):
    print(f"Your current balance is ${users[user]['balance']}")


def add_income(users: dict, path="users.json"):
    added_income = int(input("Insert amount: "))
    users[user]["balance"] += added_income
    with open(path, "w") as f:
        f.write(json.dumps(users, indent=4))
    print(Fore.GREEN + "Income added successfully!")


def logged_in_user_menu(user: str, path: str = "users.json"):
    menu = Fore.CYAN + f"""
    Hello, {user}!
    Pick an option
    1. Check balance
    2. Add income
    3. Add expenses
    4. Show list of expenses
    5. Delete profile\n"""

    user_choice = input(menu)

    with open(path, "r") as f:
        users = json.loads(f.read())
    match user_choice:
        case "1":
            print_balance(users)
        case "2":
            add_income(users)
        case "3":
            pass
        case "4":
            pass
