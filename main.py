import time
import login
import expense_tracker as trck
import progress

if __name__ == '__main__':
    while True:
        print(f"""{9 * '*'} Welcome to your expense tracker! {10 * '*'}""")
        print(f"""{17 * " "}To exit, press 9 \n""")
        time.sleep(2)
        user = login.login()
        menu = f"""
                            Hello, {user}!
                            Pick an option:
                            1. Check balance
                            2. Add income
                            3. Add expense
                            4. Show list of expenses
                            5. Remove expense
                            6. Change password
                            7. Log out\n"""
        while True:
            user_pick = input(menu)
            match user_pick:
                case "1":
                    progress.progress_bar("Checking balance...")
                    print(f" Your current balance is €{trck.check_balance()}")
                    time.sleep(2)
                case "2":
                    trck.add_income()
                    time.sleep(2)
                case "3":
                    trck.add_expense()
                    time.sleep(2)
                case "4":
                    progress.progress_bar("Showing expenses...")
                    expenses = trck.show_expenses()
                    if expenses is not None:
                        print(expenses)
                    time.sleep(2)
                case "5":
                    progress.progress_bar("Getting expenses...")
                    trck.remove_expense()
                    time.sleep(2)
                case "6":
                    login.changepwd(user)
                    time.sleep(2)
                case "7":
                    progress.progress_bar("Signing out...")
                    print("You have logged out successfully!")
                    time.sleep(2)
                    break
                case _:
                    print("Please select one of the menu options")
                    time.sleep(2)
