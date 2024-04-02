import json
from colorama import Fore


def login(path: str = "users.json") -> str:
    with open(path, "r") as f:
        list_of_users = json.loads(f.read())
    username = input(Fore.LIGHTYELLOW_EX + "Insert username: ")
    while username not in list_of_users:
        username = input(Fore.RED + "User not found! Try again: ")
    attempts = 3
    passwd = input(Fore.LIGHTYELLOW_EX + "Password: ")
    while list_of_users[username]["password"] != passwd:
        attempts -= 1
        passwd = input(Fore.RED + f"Wrong password. {attempts} attempts left. Try again: ")
        if attempts == 0:
            print(Fore.RED + "You exceeded the maximum number of attempts!")
            exit()

    return username


def add_user(path: str = "users.json"):
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


def menu_for_logged_in(user: str, path: str = "users.json"):
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
            print(f"Your current balance is ${users[user]['balance']}")
        case "2":
            added_income = int(input("Insert amount: "))
            users[user]["balance"] += added_income
            with open(path, "w") as f:
                f.write(json.dumps(users, indent=4))
            print("Income added successfully!")
        case "3":
            pass
        case "4":
            pass
        # case "5":
        #     user_pick = input("Are you sure? This will delete all the user data: ")
        #     if user_pick.lower == "y":
        #         type_pass = input("Type password: ")
        #         attempts = 3
        #         while type_pass != users[user]["password"]:
        #             attempts -= 1
        #             type_pass = input(f"Wrong password! {attempts} attempts left!  ")
        #             if attempts == 0:
        #                 print("You exceeded the maximum number of attempts!")
        #                 exit()
        #         users[user].pop()
        #         with open(path, "w") as f:
        #             f.write(json.dumps(users, indent=4))
        #         print("User deleted successfully!")




if __name__ == '__main__':
    print(Fore.LIGHTBLUE_EX + f"{10 * '*' +' '}Welcome to your budget app!{' ' + 10 * '*'}")
    login_page = Fore.GREEN + """
    1. Create new user
    2. Login with existing user\n"""
    user_pick = input(login_page)

    match user_pick:
        case "1":
            add_user()
        case "2":
            user = login()
            menu_for_logged_in(user)
