class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount