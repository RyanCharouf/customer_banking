# Accounts.py

class Account:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = 0

    def set_balance(self, new_balance):
        self.balance = new_balance

    def set_interest(self, new_interest):
        self.interest = new_interest
