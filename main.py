import my_functions


if __name__ == '__main__':
    print(f"{9 * '*'} Welcome to your budget app! {10 * '*'}")
    login_page = """
            1. Create new user
            2. Login with existing user
            3. Forgot password\n"""
    user_pick = input(login_page)

    match user_pick:
        case "1":
            my_functions.add_user_in_auth()
        case "2":
            user = my_functions.login()
            menu = f"""
            Hello, {user}!
            Pick an option:
                 1. Check balance
                 2. Add income
                 3. Add expenses
                 4. Show list of expenses
                 5. Return to main menu
                 6. Change password
                 7. Log out\n"""
            user_pick = input(menu)
            match user_pick:
                case "1": # check balance
                    my_functions.check_balance(user)
                case "2": # Add income
                    my_functions.add_income(user)
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    pass
        case "3":
            my_functions.forgot_password()
