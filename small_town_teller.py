class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"{self.id}, {self.first_name}_{self.last_name}"
    
    def __repr__(self):
        return f"{self.id}, {self.first_name}_{self.last_name}"


class Account:
    def __init__(self, number, a_type, owner, balance=0):
        self.number = number
        self.a_type = a_type
        self.owner = owner
        self.balance = balance
    
    def __repr__(self):
        return f"{self.number}, {self.a_type}, {self.owner},"


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = {}
    
    def add_customer(self, person):
        self.customers.append(person.id)
    
    def add_account(self, account):
        if account not in self.accounts:
            self.accounts[account.number] = account.balance
        else:
            print("Account already exist")
    
    def deposit(self, account_number, amount):
        self.accounts[account_number] += amount
        
        print("Amount Deposited:", amount)
    
    def withdraw(self, amount):
        self.account.balance -= amount
        
        # if self.balance >= amount:
        #    self.balance -= amount
        #    print('You Withdrew:', amount)
        # else:
        # print("Insufficient balance  ")
        print("Amount Withdrawn:", amount)
    
    def balance_inquiry(self, account_number):
        
        print(f"Available Balance= , {self.accounts[account_number]}")


zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
# zc_bank.balance_inquiry(1001)
# 0
'''zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)
# 128.02
'''
