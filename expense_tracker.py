import csv

class Expense:

    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, €{self.amount}>"

def main():
    print("Expense tracker running... ")
    expense_file_path = "expenses.csv"

    # User inputs their expense
    expense = get_user_expense()
    print(expense)
    # Add into our file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses
    summarize_expenses(expense_file_path)

def get_user_expense():
    print("Getting user expense...")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, €{expense_amount}")


    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc"
    ]

    while True:
        print("Select a category: ")
        for index, category_name in enumerate(expense_categories):
            print(f" {index + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")



def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path):
    print("Summarizing user expense...")
    with open(expense_file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Amount: {row['Amount']}, Category: {row['Category']}, Description: {row['Description']}")

if __name__ == '__main__':
    main()
