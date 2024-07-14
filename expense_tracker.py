import csv
import json
import datetime
import pandas as pd


class Expense:

    def __init__(self, name, category, amount, date_time):
        self.name = name
        self.category = category
        self.amount = amount
        self.date_time = date_time

    def __repr__(self):
        return f"Expense: {self.name}, €{self.amount}, {self.category}, {self.date_time}"


def check_balance(path="balance.json") -> float:
    with open(path, "r") as f:
        balance = json.loads(f.read())
    return balance["Balance"]


def add_income(path="balance.json"):
    with open(path, "r") as f:
        balance = json.loads(f.read())
    while True:
        try:
            income_added = float(input("Type income amount: "))
            balance["Balance"] += income_added
            with open(path, "w") as g:
                g.write(json.dumps(balance, indent=4))

            print(f"Added €{income_added} to your account. Your current balance is {balance['Balance']} ")
            break
        except Exception:
            print("The amount must be a number")


def add_expense(path="expenses.csv"):
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except Exception:
            print("Amount must be a number")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"You've entered {expense_name}, €{expense_amount} on {now}")

    expense_categories = [
        "Food", "Home", "Transport", "Fun", "Savings", "Misc"
    ]

    while True:
        print("Select a category: ")
        for index, category_name in enumerate(expense_categories):
            print(f" {index + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date_time=now)
            break
        else:
            print("Invalid category. Please try again!")

    with open(path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.date_time}\n")

    with open("balance.json", "r") as f:
        balance_dict = json.loads(f.read())
    balance_dict["Balance"] -= expense_amount
    with open("balance.json", "w") as f:
        f.write(json.dumps(balance_dict, indent=4))



    print(f"""Expense added successfully!
    Your remaining balance is {balance_dict['Balance']}
""")


def show_expenses(path="expenses.csv"):

    print(pd.options.display.max_rows)
    df = pd.read_csv(path)
    print(df.to_string())

    # with open(path, "r") as f:
    #     list_of_expenses = csv.DictReader(f)
    # for row in list_of_expenses:
    #     print(f"Time: {row['Date_time']}, Amount: {row['Amount']}, Category: {row['Category']}, Description: {row['Description']}")


