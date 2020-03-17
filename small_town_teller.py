from typing import Dict

class Person:
    def __init__(self, person_id: int, first_name: str, last_name: str):
        self.id = person_id
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"


class Account:
    def __init__(self, number: int, a_type: str, owner: Person):
        self.number = number
        self.a_type = a_type
        self.owner = owner
        self.balance = 0
    
    def __repr__(self):
        return f"{self.number}, {self.a_type}, {self.owner},"


class Bank:
    def __init__(self):
        self.customers: Dict[int, Person] = dict()
        self.accounts: Dict[int, Account] = dict()
    
    def add_customer(self, customer: Person):
        if customer.id not in self.customers:
            self.customers[customer.id] = customer.first_name, customer.last_name
        else:
            raise ValueError(f"Customer with id {customer.id} already exist.")
    
    def remove_customer(self, customer: Person):
        if customer.id in self.customers:
            del self.customers[customer.id]
        else:
            print("Customer does not exist")
    
    def add_account(self, account: Account):
        if account not in self.accounts:
            self.accounts[account.number] = account.balance
        else:
            print("Account already exist")
    
    def remove_account(self, account_number: int):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print("Account does not exist")
    
    def deposit(self, account_number: int, amount: float):
        self.accounts[account_number] += amount
        
        print("Amount Deposited:", amount)
    
    def withdrawal(self, account_number: int, amount: float):
        if account_number in self.accounts:
            self.accounts[account_number] -= amount
            print("Amount Withdrawn:", amount)
    
    def balance_inquiry(self, account_number: int):
        if account_number in self.accounts:
            print(f"Available Balance = {self.accounts[account_number]}")
        else:
            print('Invalid Account Number')


james = Person(1, 'James', 'Thompson')
bob = Person(2, 'Bob', 'Smith')
jane = Person(3, 'Jane', 'Johnson')

james_savings = Account(1001, "SAVINGS_ACCOUNT", james)
bob_checking = Account(1002, "CHECKING_ACCOUNT", bob)
jane_investment = Account(1003, "INVESTMENT_ACCOUNT", jane)

zc_bank = Bank()

zc_bank.add_customer(james)
zc_bank.add_customer(bob)
zc_bank.add_customer(jane)

zc_bank.remove_customer(bob)
zc_bank.add_customer(bob)


zc_bank.add_account(james_savings)
zc_bank.add_account(bob_checking)
zc_bank.add_account(jane_investment)

zc_bank.remove_account(1003)
zc_bank.add_account(jane_investment)

zc_bank.deposit(1003, 100)
zc_bank.deposit(1002, 500)
zc_bank.deposit(1001, 999999999)

zc_bank.withdrawal(1001, 1)
zc_bank.withdrawal(1002, 100)
zc_bank.withdrawal(1003, 50)

zc_bank.balance_inquiry(1001)
zc_bank.balance_inquiry(1002)
zc_bank.balance_inquiry(1003)