class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BankAccount:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds.")
            return None

class Transaction:
    def __init__(self, sender_account, receiver_account, amount):
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.amount = amount

class BankSystem:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.transactions = []

    def create_customer(self, customer_id, name):
        if customer_id not in self.customers:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
            return customer
        else:
            print("Customer ID already exists.")
            return None

    def create_account(self, account_number, customer_id, initial_balance=0):
        if account_number not in self.accounts:
            customer = self.customers.get(customer_id, None)
            if customer:
                account = BankAccount(account_number, customer, initial_balance)
                self.accounts[account_number] = account
                return account
            else:
                print("Customer ID not found.")
                return None
        else:
            print("Account number already exists.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number, None)
        if account:
            return account.deposit(amount)
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number, None)
        if account:
            return account.withdraw(amount)
        else:
            print("Account not found.")
            return None

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.accounts.get(sender_account_number, None)
        receiver_account = self.accounts.get(receiver_account_number, None)
        if sender_account and receiver_account:
            if sender_account.withdraw(amount):
                receiver_account.deposit(amount)
                transaction = Transaction(sender_account, receiver_account, amount)
                self.transactions.append(f'{transaction.sender_account.account_number} transferred {transaction.amount} to {transaction.receiver_account.account_number}')
                return transaction
            else:
                print("Transfer failed. Insufficient funds.")
                return None
        else:
            print("One or both accounts not found.")
            return None

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number, None)
        if account:
            return account.balance
        else:
            print("Account not found.")
            return None

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)

def main():
    bank_system = BankSystem()

    # Example customer and account creation
    customer1 = bank_system.create_customer(1, "Ahmed Awwad")
    customer2 = bank_system.create_customer(2, "Mohammed Ali")

    account1 = bank_system.create_account("AA74", 1, 1000)
    account2 = bank_system.create_account("B456", 2, 500)

    # Example deposit and withdrawal
    bank_system.deposit("AA74", 500)
    bank_system.withdraw("B456", 200)

    # Example transfer
    bank_system.transfer("AA74", "B456", 300)
    bank_system.transfer("B456", "AA74", 200)
    # Example getting account balance
    balance = bank_system.get_account_balance("AA74")
    print("Account AA74 balance:", balance)

    # Example displaying transactions
    bank_system.display_transactions()

if __name__ == "__main__":
    main()
