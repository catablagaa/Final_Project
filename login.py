import json


def read_info_from_json(path="auth.json") -> dict:
    with open(path, "r") as f:
        users = json.loads(f.read())
    return users


def changepwd(user: str):
    auth = read_info_from_json()
    while True:
        new_password = input("Insert new password: ")
        repeat = input("Write your password again: ")
        if repeat == new_password:
            print("Password updated successfully!")
            auth[f"{user.lower()}"]["password"] = new_password
            with open("auth.json", "w") as f:
                f.write(json.dumps(auth, indent=4))
            break
        else:
            print("The 2 passwords don't natch. Please try again!")


def login() -> str:
    user_info = read_info_from_json()
    username = input("Insert username: ")
    while username.lower() not in user_info:
        username = input("User not found! Try again: ")
        if username.lower() == "exit":
            exit()
    check_if_passwd_is_correct(username)

    return username


def check_if_passwd_is_correct(username: str):
    user_info = read_info_from_json()
    attempts = 3
    passwd = input(f"Insert password. You have {attempts} attempts: ")
    while user_info[username.lower()]["password"] != passwd:
        attempts -= 1
        if attempts == 0:
            print("You exceeded the maximum number of attempts!")
            exit()
        else:
            passwd = input(f"Wrong password. {attempts} attempts left. Try again: ")
