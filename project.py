# Made By Jiten :)

from sys import exit
from validator_collection import checkers
from csv import DictWriter, DictReader, reader
from re import fullmatch
from time import ctime
from pandas import read_csv
from os import mkdir, path, system
from tabulate import tabulate
from termcolor import colored
from emoji import emojize


USER = "users"
INDEX = 1000000001
database = "project_database.csv"


def main():
    system("clear")
    # My Introduction
    print()
    print("BunnyBank: Your Furry Financial Partner".center(50))
    print("My Name: Jiten".center(50))
    print("My City: Delhi".center(50))
    print("My Country: India".center(50))
    print("\n______________________________________________________")
    # Initialize Database
    initDatabase()
    # Home Page
    while True:
        print("\n______________________Main Menu______________________\n")
        print(
            tabulate(
                [
                    ["1", "Login To Your Bank Account"],
                    ["2", "Create A Bank Account"],
                    ["3", "Exit"]
                ],
                ["No.", "Options"],
                tablefmt = "rounded_grid"
            )
        )
        match bunnyAsk("Select An Option: "):
            case "1":
                system("clear")
                # Operation Page
                print("\n_________________Login To Your Account_________________\n")
                while True:
                    try:
                        userPhoneNum = bunnyAsk("Enter Your Phone Number: ")
                        userAccNum = int(bunnyAsk("Enter Your Account Number: "))
                        userPin = int(bunnyAsk("Enter Your PIN: "))
                        break
                    except ValueError:
                        bunnySay("Please, Input Valid Data")
                system("clear")
                if login(userPhoneNum, userAccNum, userPin):
                    while True:
                        print("\n____________________Operation Menu____________________\n")
                        print(
                            tabulate(
                                [
                                    ["1", "Deposit"],
                                    ["2", "Withdraw"],
                                    ["3", "Transfer Funds"],
                                    ["4", "My Information"],
                                    ["5", "Exit"]
                                ],
                                ["No.", "Options"],
                                tablefmt = "rounded_grid"
                            )
                        )
                        match bunnyAsk("Select An Option: "):
                            case "1":
                                system("clear")
                                # Deposit Money
                                print(f"\n___________________Deposit Amount___________________\n")
                                while True:
                                    try:
                                        if transaction("Deposit", int(bunnyAsk("Deposit Amount: ")), userAccNum):
                                            bunnySay("Deposit Successful :)")
                                        break
                                    except ValueError:
                                        bunnySay("Please, Input Amount in Numbers")

                            case "2":
                                system("clear")
                                # Withdraw Money
                                print(f"\n___________________Withdraw Amount___________________\n")
                                while True:
                                    try:
                                        if transaction("Withdraw", int(bunnyAsk("Withdraw Amount: ")), userAccNum):
                                            bunnySay("Withdrawal Successful :)")
                                        else:
                                            bunnySay("Withdrawal Unsuccessful :(")
                                        break
                                    except ValueError:
                                        bunnySay("Please, Input Amount in Numbers")

                            case "3":
                                system("clear")
                                # Transfer Funds
                                print("\n___________________Transfer Funds___________________\n")
                                while True:
                                    try:
                                        transferFunds(int(bunnyAsk("Transfer Amount: ")), userAccNum, int(bunnyAsk("Recipient's Account Number: ")))
                                        break
                                    except ValueError:
                                        bunnySay("Input Must Be Completely Numeric")

                            case "4":
                                system("clear")
                                # Check Account Info
                                myInfo(userAccNum)

                            case "5":
                                system("clear")
                                # Exit Operation
                                exit("\n______________The Progam Has Been Exited______________")

            case "2":
                system("clear")
                # Account Creation Page
                print("\n___________________Create An Account___________________\n")
                createBankAccount(
                    bunnyAsk("Enter Your Name: "),
                    validate("Email", bunnyAsk("Enter Your Email: ")),
                    validate("Phone Number", bunnyAsk("Enter Your Phone Number: ")),
                    validate("PIN", bunnyAsk("Create A PIN: ")),
                )

            case "3":
                system("clear")
                # Exit Operation
                exit("\n______________The Progam Has Been Exited______________")




# Initialize Database If It Not Initialized Yet
def initDatabase():
    try:
        with open(database) as db:
            pass
    except FileNotFoundError:
        with open(database, "w") as db:
            db.write("name,email,phoneNum,pin,money\n")
        mkdir(USER)




# Stores Client's Data In Database And Assigns An Account Number To The Client
def createBankAccount(name, email, phoneNum, pin, money = 0):
    # Add Client Data To The Database
    with open(database, "a") as db:
        writer = DictWriter(db, fieldnames = ["name", "email", "phoneNum", "pin", "money"])
        writer.writerow({"name" : name,
                         "email" : email,
                         "phoneNum" : phoneNum,
                         "pin" : pin,
                         "money" : money})
    # Notify The User About Their Account Number
    with open(database) as db:
        reader = DictReader(db)
        for accNum, _ in enumerate(reader, INDEX):
            pass
    bunnySay(f"Congrats! {name.title()}, Your Account has been created. Your Account Number is {accNum}")
    # Creating User's Transaction History Database
    with open(path.join(USER, f"{name}{accNum}.csv"), "w") as user:
        user.write("Time,Operation,Money\n")




# This Function Gets Users Data And Login To User's Account
def login(phoneNum, accNum, pin):
    with open(database) as cDB:
        dbReader = DictReader(cDB)
        for accIndex, client in enumerate(dbReader, 1000000001):
            if phoneNum == client["phoneNum"] and accNum == accIndex and pin == int(client["pin"]):
                bunnySay(f"Welcome, {client['name'].title()}")
                return True
        bunnySay("Invalid Credentials!")
        return False




# This Function Validate Email, Phone Number and PIN Inputed By The User While Creating An Account
def validate(prompt, obj):
    while True:
        if prompt == "Email" and checkers.is_email(obj) or prompt == "Phone Number" and fullmatch(r"\+?[ ()\d-]+", obj) or prompt == "PIN" and obj.isnumeric():
            return obj
        bunnySay(f"Your {prompt} Was Invalid")
        obj = bunnyAsk(f"Please Enter Valid {prompt}: ")




# This Function Provide Transaction Operations Like Deposit And Withdrawal
def transaction(operation, operand, accNum):
    if operand < 0:
        operand = -operand
    db = read_csv(database)
    for i in range(len(db)):
        if i == accNum - INDEX:
            if operation == "Deposit":
                db.loc[i, "money"] += operand
                with open(path.join(USER, f"{db.loc[i, 'name']}{accNum}.csv"), "a") as user:
                    writer = DictWriter(user, fieldnames = ["Time","Operation","Money"])
                    writer.writerow({"Time": ctime(),
                                        "Operation": colored(f"+{operand}", "green"),
                                        "Money" : db.loc[i, "money"]})
            elif operation == "Withdraw":
                if db.loc[i, "money"] >= operand:
                    db.loc[i, "money"] -= operand
                    with open(path.join(USER, f"{db.loc[i, 'name']}{accNum}.csv"), "a") as user:
                        writer = DictWriter(user, fieldnames = ["Time","Operation","Money"])
                        writer.writerow({"Time": ctime(),
                                         "Operation": colored(f"-{operand}", "red"),
                                         "Money" : db.loc[i, "money"]})
                else:
                    bunnySay("Not Enough Balance In Your Bank Account To Make This Transaction")
                    return False
            break
    db.to_csv(database, index = False)
    return True




# This Function Transfer Funds From One Account To Another
def transferFunds(amount, userAccNum, recAccNum):
    db = read_csv(database)
    if not(0 < recAccNum - (INDEX - 1) <= len(db)):
        bunnySay("Recipient's Account Doesn't Exist")
        return False
    if transaction("Withdraw", amount, userAccNum):
        transaction("Deposit", amount, recAccNum)
        bunnySay(f"Transfer Successful :)")




# This Function Shows The Information Of My Account
def myInfo(accNum, currency = emojize(":carrot:")):
    print("\n___________________My Information___________________\n")
    db = read_csv(database)
    for i in range(len(db)):
        if i == accNum - INDEX:
            print(f"Name: {db.loc[i, 'name'].title()}")
            print(f"Email: {db.loc[i, 'email']}")
            print(f"Phone Number: {db.loc[i, 'phoneNum']}")
            print(f"Amount In Your Account: {db.loc[i, 'money']}{currency}")
            break
    print("\n\t___________Transaction History___________\n")
    with open(path.join(USER, f"{db.loc[i, 'name']}{accNum}.csv")) as user:
        userReader = reader(user)
        print(tabulate(userReader, headers = "firstrow", tablefmt = "rounded_grid"))




# Mr. Bunny Saying Something To Us
def bunnySay(prompt):
    print(f"\n\t< {prompt} >\n(\\__/)  /\n( •.•) /\n/>  <\\")




# Mr. Bunny Asking Us Something
def bunnyAsk(prompt):
    print("\n(\\__/)\n( •.•)\n/>   \\> ", end = "")
    return input(prompt).strip()




if __name__ == "__main__":
    main()
