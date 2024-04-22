import json


def read_info_from_file(path="users.json") -> dict:
    with open(path, "r") as f:
        users = json.loads(f.read())
        return users


def login(path: str = "auth.json") -> str:
    with open(path, "r") as f:
        list_of_users = json.loads(f.read())
    username = input("Insert username: ")
    while username.lower() not in list_of_users:
        username = input("User not found! Try again: ")
    attempts = 3
    passwd = input("Password: ")
    while list_of_users[username.lower()] != passwd:
        attempts -= 1
        passwd = input(f"Wrong password. {attempts} attempts left. Try again: ")
        if attempts == 0:
            print("You exceeded the maximum number of attempts!")
            exit()

    return username


def add_user_in_auth(path: str = "auth.json"):
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
    new_user = {username: passwd}
    list_of_users.update(new_user)
    with open(path, "w") as f:
        f.write(json.dumps(list_of_users, indent=4))
    print("User added successfully!")


def check_balance(user):
    users = read_info_from_file()
    print(f"Your current balance is ${users[user]['balance']}")


def add_income(users: dict, user, path="users.json"):
    added_income = int(input("Insert amount: "))
    users[user]["balance"] += added_income
    with open(path, "w") as f:
        f.write(json.dumps(users, indent=4))
    print("Income added successfully!")


# def logged_in_user_menu(user: str, path: str = "users.json"):
#     menu = f"""
#     Hello, {user}!
#     Pick an option
#     1. Check balance
#     2. Add income
#     3. Add expenses
#     4. Show list of expenses\n"""
#
#     user_choice = input(menu)
#
#     with open(path, "r") as f:
#         users = json.loads(f.read())
#     match user_choice:
#         case "1":
#             print_balance(user)
#         case "2":
#             add_income(user)
#         case "3":
#             pass
#         case "4":
#             pass
