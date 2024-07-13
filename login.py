import json


def read_info_from_users(path="auth.json") -> dict:
    with open(path, "r") as f:
        users = json.loads(f.read())
    return users


def changepwd(path="auth.json"):
    auth = read_info_from_users()
    while True:
        new_password = input("Insert new password: ")
        repeat = input("Write your password again: ")
        if repeat == new_password:
            print("Password updated successfully!")
            break
        else:
            print("The 2 passwords don't natch. Please try again!")


def login(path: str = "auth.json") -> str:
    user_info = read_info_from_users()
    username = input("Insert username: ")
    while username.lower() not in user_info:
        username = input("User not found! Try again: ")
        if username.lower() == "exit":
            exit()
    check_if_passwd_is_correct(username)

    return username


def check_if_passwd_is_correct(username):
    user_info = read_info_from_users()
    attempts = 3
    passwd = input(f"Insert password. You have {attempts} attempts: ")
    while user_info[username.lower()]["password"] != passwd:
        attempts -= 1
        if attempts == 0:
            print("You exceeded the maximum number of attempts!")
            exit()
        else:
            passwd = input(f"Wrong password. {attempts} attempts left. Try again: ")

# def add_user_in_auth(path: str = "auth.json"):
#     users = read_info_from_users("auth.json")
#
#     username = input("Choose your username: ")
#     while username in users:
#         username = input("Username taken. Please try another one:")
#     passwd = " "
#     confirm = "a"
#     while passwd != confirm:
#         passwd = input("Create password: ")
#         confirm = input("Confirm password: ")
#         if passwd != confirm:
#             print("Passwords don't match! ")
#         else:
#             break
#     email_address = input("What's your eamil address? ")
#     user_pick = input(questions.security_questions)
#     match user_pick:
#         case "1":
#             answer = input("Answer: ")
#             new_user = {username: {"password": passwd, "security question": {"q": questions.security_questions_list[0], "a": answer},
#                                    "email": email_address}}
#             users.update(new_user)
#         case "2":
#             answer = input("Answer: ")
#             new_user = {
#                 username: {"password": passwd, "security question": {"q": questions.security_questions_list[1], "a": answer},
#                            "email": email_address}}
#             users.update(new_user)
#         case "3":
#             answer = input("Answer: ")
#             new_user = {
#                 username: {"password": passwd, "security question": {"q": questions.security_questions_list[2], "a": answer},
#                            "email": email_address}}
#             users.update(new_user)
#         case "4":
#             answer = input("Answer: ")
#             new_user = {
#                 username: {"password": passwd, "security question": {"q": questions.security_questions_list[3], "a": answer},
#                            "email": email_address}}
#             users.update(new_user)
#         case "5":
#             answer = input("Answer: ")
#             new_user = {
#                 username: {"password": passwd, "security question": {"q": questions.security_questions_list[4], "a": answer},
#                            "email": email_address}}
#             users.update(new_user)
#
#     with open(path, "w") as f:
#         f.write(json.dumps(users, indent=4))
#     print("User added successfully!")
#
#
# def add_income(user, path="users.json"):
#     users = read_info_from_users()
#     added_income = float(input("Insert amount: "))
#     users[user]["balance"] += added_income
#     with open(path, "w") as f:
#         f.write(json.dumps(users, indent=4))
#     print(f"${added_income} added successfully!")
#
#
# def forgot_password():
#     users = read_info_from_users(path="auth.json")
#     username = input("Insert username: ")
#     while username not in users:
#         username = input("This user doesn't exist. Try again:")
#     answer = input(f"""Please answer this security question:
# {users[username]["security question"]["q"]} """)
#     attempts = 3
#     while answer != users[username]["security question"]["a"]:
#         attempts -= 1
#         answer = input(f"Wrong answer, {attempts} attempts left: ")
#         if attempts == 1:
#             print("You exceeded the max number of attempts.")
#             exit()
#     print(f'Your password is {users[username]["password"]}')
