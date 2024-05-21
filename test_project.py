# Made By Jiten :)

from project import initDatabase, createBankAccount, validate, transaction

def test_createBankAccount():
    initDatabase()
    createBankAccount("Jiten", "denji.chainsawman@gmail.com", "9999900000", "1234")
    with open("project_database.csv") as db:
        for i in db:
            pass
    assert i == "Jiten,denji.chainsawman@gmail.com,9999900000,1234,0\n"


def test_validate():
    assert validate("Email", "denji.chainsawman@gmail.com") == "denji.chainsawman@gmail.com"
    assert validate("Phone Number", "(555) 555-1234") == "(555) 555-1234"
    assert validate("Phone Number", "9171477140") == "9171477140"
    assert validate("PIN", "1234") == "1234"


def test_transaction():
    assert transaction("Deposit", 10000, 1000000001) == True
