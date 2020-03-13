class Person:
    def__init__(self, id, first_name, last_name):
        self.id =
        self.first_name =
        self.last_name =



class Acccount:
    def__init__(self, number, type, owner, balance):
        self.number = 
        self.type =
        self.owner =
        self.balance =
        self.Person =


class Bank:
    def__init__(self, add_customer, add_account):
        self.add_customer
        self.add_account
        self.Acccount
        self.

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





        
