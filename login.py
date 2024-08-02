from expense_tracker import load_json, write_json
import progress
import pyautogui


def login() -> str:
    user_info = load_json("auth.json")
    config = load_json("config.json")
    attempts = config["attempts"]
    username = input("Insert username: ")

    if username == "9":
        exit()

    while username.lower() not in user_info:
        username = input("User not found! Try again: ")

    passwd = pyautogui.password(text=f'Insert password. You have {attempts} attempts.', title='Password', default='', mask='*')

    while passwd != user_info[f"{username.lower()}"]["password"]:
        attempts -= 1
        if attempts == 0:
            print("You have exceeded the maximum number of attempts.")
            exit()
        passwd = pyautogui.password(text=f'Wrong password. You have {attempts} attempts left. Try again: ', title='',
                                    default='', mask='*')
    progress.progress_bar("Signing in...")
    return username


def changepwd(user: str):

    auth = load_json("auth.json")

    while True:
        while True:
            new_password = pyautogui.password(text='Insert new password: ',
                                        title='', default='', mask='*')
            if new_password != auth[f'{user}']['password']:
                break
            else:
                print("The new password cannot be the same as the current one")
        repeat = pyautogui.password(text='Write your password again: ',
                                        title='', default='', mask='*')
        if repeat == new_password:
            progress.progress_bar("Updating password...")
            print("Password updated successfully!")
            auth[f"{user.lower()}"]["password"] = new_password
            write_json(auth, "auth.json")
            break
        else:
            print("The 2 passwords don't match. Please try again!")
