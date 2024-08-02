import json
import datetime
import pandas as pd
import progress


class Expense:
    def __init__(self, name, category, amount, date_time):
        self.name = name
        self.category = category
        self.amount = amount
        self.date_time = date_time

    def __repr__(self):
        return (f"Expense name: {self.name}, amount: €{self.amount}, "
                f"category: {self.category}, date and time: {self.date_time}")


# Reads information from json file
def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.loads(f.read())


# Writes info to json file
def write_json(data, path: str, action="w"):
    with open(path, f"{action}") as f:
        f.write(json.dumps(data, indent=4))


# checks balance
def check_balance(path: str="balance.json") -> float:
    balance = load_json(path)
    return balance["Balance"]


def add_income(path: str = "balance.json"):
    # loads info from json file
    balance = load_json(path)
    while True:
        try:
            income_added = float(input("Type income amount: "))
            confirmation = input(f"You are adding €{income_added} to your account. "
                                 f"To confirm, press Y, to change, press any key: ")
            if confirmation.lower() == "y":
                balance["Balance"] += income_added
                progress.progress_bar("Adding income...")
                write_json(balance, path)
                print(f"Added €{income_added} to your account. Your current balance is {balance['Balance']} ")
                break
        except Exception:
            print("The amount must be a number")


def add_expense(path: str = "expenses.csv"):
    while True:
        # Checks if the expense name is blank. If it is, it shows an error message
        while True:
            expense_name = input("Enter expense name: ")
            if expense_name != "":
                break
            else:
                print("Expense name cannot be blank.")
        # Gets amount and checks if it is a number
        while True:
            try:
                expense_amount = float(input("Enter expense amount: "))
                break
            except Exception:
                print("Amount must be a number")

        # This part takes the categories from config and the date and time of the device
        config = load_json("config.json")
        expense_categories = config["expense_categories"]
        now = datetime.datetime.now().strftime(f"{config['date_time_format']}")


        # Select category
        while True:
            print("Select a category: ")
            for index, category_name in enumerate(expense_categories):
                print(f" {index + 1}. {category_name}")

            value_range = f"1 and {len(expense_categories)}"

            while True:
                try:
                    selected_index = int(input(f"Enter a category number between {value_range}: ")) - 1
                    break
                except Exception:
                    print("Please type only the number of the category.")


            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date_time=now)
                print(f"You're entering {expense}")
                break
            else:
                print("Invalid category. Please try again!")

        add_to_file = input("To confirm, press 1. To cancel, press any other key: ")

        # Adds expense to file
        if add_to_file == "1":
            with open("expenses.csv", "a") as f:
                f.write(f"{expense.date_time},{expense.name},{expense.amount},{expense.category}\n")

            balance_dict = load_json("balance.json")
            balance_dict["Balance"] -= expense_amount
            write_json(balance_dict, "balance.json", "w")
            break
        else:
            continue
    progress.progress_bar("Adding expense...")
    print(f"""Expense added successfully!
    Your remaining balance is {balance_dict['Balance']}
""")


def show_expenses(path="expenses.csv") -> pd:
    df = pd.read_csv(path)
    if df.empty:
        print("No expenses to show.")
    else:
        df.index = range(1, len(df) + 1)
        return df


def remove_expense(path="expenses.csv"):
    df = show_expenses()
    if df.empty:
        print("No expenses to remove.")
    print(df.to_string())
    while True:
        try:
            user_pick = int(input("Insert the ID of the expense that you want to remove: "))
            if 1 <= user_pick <= len(df):
                df.drop(user_pick, axis=0, inplace=True)
                df.to_csv(path, index=False)
                progress.progress_bar("Removing expense...")
                print("Expense removed successfully!")
                break
        except Exception:
            print("Please type only the index number of the expense you want to remove. ")
