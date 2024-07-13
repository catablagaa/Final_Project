import login
import expense_tracker as trck


if __name__ == '__main__':
    while True:
        print(f"{9 * '*'} Welcome to your expense tracker! {10 * '*'}")
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
        user_pick = input(menu)
        match user_pick:
            case "1":
                print(f" Your current balance is {trck.check_balance()}")
            case "2":
                trck.add_income()
            case "3":
                expense = trck.add_expense()
                trck.save_expense_to_file(expense)
            case "4":
                trck.show_expenses()
            case "5":
                pass
            case "6":
                login.changepwd()
            case "7":
                continue







        # login_page = """
        #         1. Create new user
        #         2. Login with existing user
        #         3. Forgot password\n"""
        # user_pick = input(login_page)
        #
        # match user_pick:
        #     case "1":
        #         my_functions.add_user_in_auth()
        #     case "2":

        #
        #         match user_pick:
        #             case "1": # check balance
        #                 my_functions.check_balance(user)
        #             case "2": # Add income
        #                 my_functions.add_income(user)
        #             case "3": #Add expense
        #                 pass
        #             case "4":
        #                 pass
        #             case "5":
        #                 pass
        #             case "6":
        #                 pass
        #             case "7":
        #                 pass
        #     case "3":
        #         my_functions.forgot_password()
