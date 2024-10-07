from operator import truediv
from random import randint

print("Welcome to GTB BANK")
accountNumbers = []
firstNames = []
lastNames = []
Balances = []
pins = []

print("Please select an option:")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Check Balance")
print("5. Transfer Money")
print("6. Change PIN")
print("7. Close Account")
print("8. Exit")

def show_choice():
    exist = "false"
    while not exist:
        show_choice()
try:
    show_choice()
    choice = int(input("select an option: "))
    if choice == 1:
        print("you selected: create Account")
    if choice == 2:
        print("you selected: deposit Money")
    if choice == 3:
        print("you selected: withdraw Money")
    if choice == 4:
        print("you selected: check Balance")
    if choice == 5:
        print("you selected: transfer Money")
    if choice == 6:
        print("you selected: change pin")
    if choice == 7:
         print("you selected: close Account")
    if choice == 8:
         print("you closed")

except ValueError:
        print("invalid option input number from 1 to 8")
        print("Thank you for using GTB Bank")

if choice == 1:
    # Create Account
    print("\n--- Create an Account ---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = randint(1000000, 9999999)

    while True:
        try:
            pin = int(input("Set a 4-digit PIN: "))
            if 1000 <= pin <= 9999:
                break
            else:
                print("Invalid PIN. Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Store account details
    accountNumbers.append(account_number)
    firstNames.append(first_name)
    lastNames.append(last_name)
    pins.append(pin)
    Balances.append(0.0)
print(f"Account created successfully! Your account number is {accountNumbers}")
print("Account Create Successfully ")

if choice == 2:
# Deposit Money
    print("\n--- Deposit Money ---")
account_number = int(input("Enter your account number: "))
if account_number in accountNumbers:
    index = accountNumbers.index(account_number)
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0.0:
        Balances[index] += amount
        print(f"Deposit successful! New balance: {Balances[index]}")
    else:
        print("Invalid amount. Please enter a positive number.")
else:
    print("Account number not found.")

if choice == 3:
    # Withdraw Money
    print("\n--- Withdraw Money ---")
    account_number = int(input("Enter your account number: "))
if account_number in accountNumbers:
    index = accountNumbers.index(account_number)
    pin = int(input("Enter your PIN: "))
    if pins[index] == pin:
        amount = float(input("Enter the amount to withdraw: "))
    if 0 < amount <= Balances[index]:
        Balances[index] -= amount
    print(f"Withdrawal successful! New balance: {Balances[index]}")

else:
    print("Insufficient balance or invalid amount.")


if choice == 4:
    print("\n--- check Balance ---")
    account_number = int(input("Enter your account number: "))
    if account_number in accountNumbers:
        index = accountNumbers.index(account_number)
        pin = int(input("Enter your PIN: "))
        if pins[index] == pin:
            print(f"Your balance is: {Balances[index]}")
        else:
            print("Incorrect PIN!")
    else:
        print("Account number not found.")

if choice == 5:
    print("\n--- Transfer Money ---")
    sender_account = int(input("Enter your account number: "))
    if sender_account in accountNumbers:
        sender_index = accountNumbers.index(sender_account)
        recipient_account = int(input("Enter the recipient's account number: "))
        if recipient_account in accountNumbers:
            recipient_index = accountNumbers.index(recipient_account)
            amount = float(input("Enter the amount to transfer: "))
            if 0 < amount <= Balances[sender_index]:
                Balances[sender_index] -= amount
                Balances[recipient_index] += amount
                print(f"Transfer successful! You transferred {amount} to account {recipient_account}.")
                print(f"Your new balance is: {Balances[sender_index]}")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Recipient account number not found.")
    else:
        print("Your account number not found.")
if choice == 6:
    print("\n--- Change PIN ---")
    account_number = int(input("Enter your account number: "))
    if account_number in accountNumbers:
        index = accountNumbers.index(account_number)
        current_pin = input("Enter your current PIN: ")
        if current_pin == pins[index]:
            while True:
                new_pin = input("Enter a new 4-digit pin: ")
                if new_pin.isdigit() and 1000 <= int(new_pin) <= 9999:
                    pins[index] = new_pin
                    print("PIN changed successfully!")
                    break
                else:
                    print("Invalid pin. Please enter a 4-digit number.")
        else:
            print("Incorrect current PIN.")
    else:
        print("Account number not found.")

if choice == 7:
    print("\n--- Close Account---")
    account_number = int(input("Enter your account number: "))
    if account_number in accountNumbers:
        index = accountNumbers.index(account_number)
        confirm = input(f"Are you sure you want to close the account {account_number}? (yes/no): ")
        if confirm.lower() == "yes":
            accountNumbers.pop(index)
            firstNames.pop(index)
            lastNames.pop(index)
            Balances.pop(index)
            pins.pop(index)
            print("Account closed successfully!")
        else:
            print("Account closure canceled.")
    else:
        print("Account number not found.")

if choice == 8:
    print("Thank you for using GTB Bank! Goodbye!")






