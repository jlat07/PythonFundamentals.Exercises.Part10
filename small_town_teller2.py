from typing import Dict
import pickle


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
            self.customers[customer.id] = customer
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
    
    def save_data(self):
        PersistenceUtils.write_pickle("customers.pickle", self.customers)
        PersistenceUtils.write_pickle("accounts.pickle", self.accounts)
    
    def load_data(self):
        self.customers = PersistenceUtils.load_pickle("customers.pickle")
        self.accounts = PersistenceUtils.load_pickle("accounts.pickle")


class PersistenceUtils:
    
    def __init__(self):
        pass
    
    @staticmethod
    def write_pickle(file_name, data):
        with open(file_name, "wb") as handler:
            pickle.dump(data, handler)
        print('Data Saved')
    
    @staticmethod
    def load_pickle(pickle_file):
        with open(pickle_file, 'rb') as handler:
            data = pickle.load(handler)
        return data
        print("Data Loaded")
