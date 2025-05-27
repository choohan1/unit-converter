streamlit as st
from atm import ATM
123class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin

    def verify_pin(self, entered_pin):
        """Verify if the entered PIN is correct."""
        return entered_pin == self.pin

    def check_balance(self):
        """Return the current balance."""
        return f"Your current balance is ${self.balance:.2f}"

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def run(self):
        """Main ATM interface loop."""
        print("Welcome to the ATM")
        
        # PIN verification
        for _ in range(3):  # Allow 3 attempts
            entered_pin = input("Enter your PIN: ")
            if self.verify_pin(entered_pin):
                break
            print("Incorrect PIN. Try again.")
        else:
            print("Too many incorrect attempts. Card blocked.")
            return

        # Main menu
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ")
            
            if choice == "1":
                print(self.check_balance())
            
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    print(self.deposit(amount))
                except ValueError:
                    print("Please enter a valid numeric amount.")
            
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    print(self.withdraw(amount))
                except ValueError:
                    print("Please enter a valid numeric amount.")
            
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            
            else:
                print("Invalid option. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()