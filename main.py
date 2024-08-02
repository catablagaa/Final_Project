import login
import expense_tracker as trck

# In terminal pentru a transforma din gui in py:
# pyuic6 -x .\roady_gui.ui -o roady_gui.py



if __name__ == '__main__':
    while True:
        print(f"{9 * '*'} Welcome to your expense tracker! {10 * '*'}")
        user = login.login()
        while True:
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
                    print(f" Your current balance is €{trck.check_balance()}")
                case "2":
                    trck.add_income()
                case "3":
                    trck.add_expense()
                case "4":
                    trck.show_expenses()
                case "5":
                    pass
                case "6":
                    login.changepwd(user)
                case "7":
                    break
