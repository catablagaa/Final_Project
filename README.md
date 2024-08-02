# Expense Tracker

## Overview

Welcome to the Expense Tracker, a command-line application designed to help you manage your finances efficiently. This tool allows you to log in, track your income and expenses, and maintain an updated balance.

## Features

- **User Authentication**: Secure login system with password protection.
- **Balance Tracking**: Check your current balance anytime.
- **Income Management**: Add income to your account.
- **Expense Management**: Add, view, and remove expenses.
- **Password Management**: Change your password securely.
- **Progress Feedback**: Visual progress bars to enhance user experience.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Install the required packages:
   ```shell
   pip install -r requirements.txt

2. Ensure the following files are present in the project directory:
- main.py
- login.py
- expense_tracker.py
- progress.py
- auth.json
- config.json
- balance.json
- expenses.csv

### Running the Application

Start the application by running the main.py script

## File descriptions:
### 'main.py'

This is the entry point of the application. It handles user interaction and navigation through different functionalities like checking balance, adding income, adding or removing expenses, and changing passwords.

### 'login.py'
Handles user authentication and password management:

- login(): Authenticates the user.
- changepwd(user): Allows the user to change their password. 

### expense_tracker.py
Manages all expense tracking functionalities:

- check_balance(): Checks the current balance.
- add_income(): Adds income to the account.
- add_expense(): Adds an expense to the account.
- show_expenses(): Displays a list of all expenses.
- remove_expense(): Removes an expense from the account. 

### progress.py
Provides visual feedback for operations using progress bars:

- progress_bar(message): Displays a progress bar with the given message.


### auth.json
Stores user authentication data:

```shell
{
    "john": {
        "password": "1234",
        "email": "abc@example.com"
    }
}
```

### config.json
Stores configuration settings for the application:
```shell
{
  "expense_categories": ["Food", "Home", "Transport", "Fun", "Savings", "Misc", "Housekeeping"],
  "date_time_format": "%Y-%m-%d %H:%M",
  "attempts": 3
}
```
In this file, you can: 
- change the number of possible attempts to type the password
- update the categories (make sure that the text is formatted properly)
- update the date and time format

### balance.json
Stores the current balance:
```shell
{
    "Balance": 1034.73
}
```

### expenses.csv
Stores the list of expenses:
```shell
Date_time,Name,Amount,Category
2024-07-31 11:41,bill,12.0,Food
2024-07-31 11:45,juice,5.0,Food
2024-07-31 12:05,limes,12.0,Food
2024-07-31 13:08,rent,1123.0,Home
```


## Usage

Upon running main.py, you will be prompted to log in. Once authenticated, you can navigate through the menu to check your balance, add income or expenses, view or remove expenses, and change your password. To log out, select the appropriate option from the menu.


## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

