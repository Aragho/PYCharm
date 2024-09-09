from decimal import Decimal


class Account:

    def __init__(self, name, pin, balance = 0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance


    def deposit(self, amount):
        if amount < Decimal(0.00):
            raise ValueError("Amount cannot be less than zero")

        self.balance += amount


account1 = Account( "adenike", "1111")
account2 = Account( "Dunni", "0000")
account1.deposit(5000)
print(account1.balance)



