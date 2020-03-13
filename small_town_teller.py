class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name



class Acccount:
    def __init__ (self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance
        self.Person = Person


class Bank:
    def __init__(self, add_customer, add_account):
        self.add_customer = add_customer
        self.add_account = add_account
 
    # Function to deposite amount 
    def deposit(self): 

        amount = float(input("Enter amount to be deposited: ")) 
        
        self.balance += amount 

        print("Amount Deposited:", amount) 

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 
            self.balance-=amount 
            print("You Withdrew:", amount) 
        else: 
            print("Insufficient balance  ") 
  
    
    def balance_inquiry(self): 

        print("Net Available Balance=",self.balance) 





        
