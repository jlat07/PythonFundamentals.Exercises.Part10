class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance = 0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

class Bank():
    cust = []
    acct = {}
    acct_type = ['CHECKING', 'SAVINGS']

    def add_customer(self, person):
        if person.id not in self.cust:
            self.cust.append(person.id)
        else:
            print('That ID already exists')

    def add_account(self, account):
        if account not in self.acct:
            self.acct[account.number] = account.balance

    def remove_account(self, account):
        if account in self.acct:
            del[self.acct[account]]

    def deposit(self, account, amount):
        self.acct[account] += amount

    def withdraw(self, account, amount):
        if amount <= self.acct[account]:
            self.acct[account] -= amount
        else:
            print("Insufficient funds")
            print("Your max withdrawal amount is {self.balance-self.withdraw_amount}")

    def balance_inquiry(self, account):
        print(f"Balance: {self.acct[account]}")