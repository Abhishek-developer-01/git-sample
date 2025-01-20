class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []  # List to store transaction history

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append({"type": "Deposit", "amount": amount, "balance": self.balance})
            print(f"Rs. {amount} deposited successfully. New balance: Rs. {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append({"type": "Withdrawal", "amount": amount, "balance": self.balance})
            print(f"Rs. {amount} withdrawn successfully. New balance: Rs. {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: Rs. {self.balance}")

    def display_transaction_history(self):
        if not self.transactions:
            print("\nNo transactions available.")
            return

        print("\nTransaction History:")
        print("Type       | Amount   | Balance After")
        print("--------------------------------------")
        for transaction in self.transactions:
            print(f"{transaction['type']:10} | Rs. {transaction['amount']:7} | Rs. {transaction['balance']:12}")

class BankingManagementSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists. Try a different number.")
            return

        name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))

        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return

        account = BankAccount(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        print("Account created successfully.")

    def access_account(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)

        if not account:
            print("Account not found.")
            return

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display Account Details")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                account.display_details()
            elif choice == '4':
                account.display_transaction_history()
            elif choice == '5':
                print("Exiting account management.")
                break
            else:
                print("Invalid choice. Please try again.")

    def start(self):
        while True:
            print("\nBanking Management System")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.access_account()
            elif choice == '3':
                print("Thank you for using the Banking Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    BankingManagementSystem().start()
'''
The Banking Management System code has been updated to include all requested features, including transaction history. Users can now:

Create Accounts: Add new accounts with initial deposits.
Access Accounts: Perform deposits, withdrawals, and view account details.
Transaction History: Track and display a detailed history of all transactions
'''
