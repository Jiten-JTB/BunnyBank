# BunnyBank: Your Furry Financial Partner! 🐰
#### Video Demo:  [My CS50 Final Project](https://youtu.be/GKqIcUmg3dE?si%253DOk_AtNPqz_dsoQ5P)
#### Description:
BunnyBank is a Bunny themed user-friendly command-line banking application created by Jiten. It allows users to perform basic banking operations, such as creating a bank account, depositing money, withdrawing funds, transferring funds, and checking their account information as well as transaction history.

## Developer Information

- **Developer:** Jiten
- **City:** Delhi
- **Country:** India

## Features

- **Login and Account Creation:** Users can log in to their bank accounts with their phone number, account number, and PIN. They can also create a new bank account with their name, email, phone number, and PIN.

- **Deposit and Withdrawal:** Users can deposit and withdraw money from their accounts.

- **Fund Transfer:** Users can transfer funds from their account to another user's account.

- **Account Information:** Users can check their account information, including name, email, phone number, account balance and transaction history.

## How to Run

1. Run `pip install -r requirements.txt` to install dependency libraries.
2. Execute `project.py` to start the BunnyBank application.
3. Follow the on-screen instructions to log in or create a new account.
4. Perform banking operations as needed.

 ## Database Initialization

When you run `project.py`, the `initDatabase` function checks for the existence of a database file named `project_database.csv`. If it doesn't exist, the function creates it with necessary headers and sets up the `users` folder for storing user transaction history.

## Transaction History

The application stores user transaction history in the `users` folder. Each user has a separate CSV file containing their transaction records.

## Dependencies

- `validator_collection`: A Python library for data validation.
- `pandas`: A powerful data manipulation library.
- `tabulate`: For formatting and displaying data as tables.
- `termcolor`: For adding colored text to the console.
- `emoji`: For adding emojis to the output.
