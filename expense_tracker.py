import csv
import json
import datetime

class Expense:

    def __init__(self, name, category, amount, date_time):
        self.name = name
        self.category = category
        self.amount = amount
        self.date_time = date_time

    def __repr__(self):
        return f"Expense: {self.name}, €{self.amount}, {self.category}, {self.date_time}"

def main():
    print("Expense tracker running... ")
    expense_file_path = "expenses.csv"

    # User inputs their expense
    expense = add_expense()
    print(expense)
    # Add into our file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses
    show_expenses(expense_file_path)


def check_balance(path="balance.json"):
    with open(path,"r") as f:
        balance = json.loads(f.read())
    return balance["Balance"]


def add_income(path="balance.json"):
    with open(path,"r") as f:
        balance = json.loads(f.read())

    income_added = float(input("Type income amount: "))
    balance["Balance"] += income_added
    with open(path, "w") as g:
        g.write(json.dumps(balance, indent=4))

    print(f"Added €{income_added} to your account. Your current balance is {balance['Balance']} ")



def add_expense():
    print("Getting user expense...")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"You've entered {expense_name}, €{expense_amount} on {now}")


    expense_categories = [
        "Food", "Home", "Work", "Transport", "Fun", "Misc"
    ]

    while True:
        print("Select a category: ")
        for index, category_name in enumerate(expense_categories):
            print(f" {index + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date_time=now)
            return new_expense
        else:
            print("Invalid category. Please try again!")



def save_expense_to_file(expense: Expense, expense_file_path = "expenses.csv"):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.date_time}\n")

    with open("balance.json", "r") as f:
        balance_dict = f.read()
    balance_dict["Balance"] -= expense.amount

    with open("balance.json", "w") as g:
        g.write(json.dumps(balance_dict, indent=4))




def show_expenses(expense_file_path = "expenses.csv"):
    print("Getting your expenses...")
    with open(expense_file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Time: {row['Date_time']}, Amount: {row['Amount']}, Category: {row['Category']}, Description: {row['Description']}")


def remove_expense():
    pass