import json
import pickle


class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"


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
        if person.id not in self.customers:
            self.customers.append(person.id)
        else:
            print("Customer ID already exist")
    
    def remove_customer(self, person):
        if person.id in self.customers:
            self.customers.remove(person.id)
        else:
            print("Customer does not exist")
    
    def add_account(self, account):
        if account not in self.accounts:
            self.accounts[account.number] = account.balance
        else:
            print("Account already exist")
    
    def remove_account(self, account):
        if account in self.accounts:
            del self.accounts[account.number]
        else:
            print("Account does not exist")
    
    def deposit(self, account_number, amount):
        self.accounts[account_number] += amount
        
        print("Amount Deposited:", amount)
    
    def withdrawal(self, account_number, amount):
        self.accounts[account_number] -= amount
        if amount > self.accounts[account_number]:
            print("Insufficient balance")
        else:
            self.accounts[account_number] -= amount
            print("Amount Withdrawn:", amount)
    
    def balance_inquiry(self, account_number):
        print(f"Available Balance= {self.accounts[account_number]}")