
class Bank:
...     def __init__(self):
...         self.customers = []
...         self.accounts = []
...     
...     def add_customer(self, customer):
...         self.customers.append(customer)
...         


zc_bank = Bank()
zc_bank.customers
[]
zc_bank.add_customer('Bob')
zc_bank.customers
['Bob']


class Person:
...     def __init__(self, id, first_name, last_name):
...         self.id = id
...         self.first_name = first_name
...         self.last_name = last_name
...         

James = Person(1, "James", "Thompson")
James.id
1
James.first_name
'James'
James.last_name
'Thompson'

zc_bank.add_customer(James)
zc_bank.customers
['James', <__main__.Person object at 0x105712ef0>]
print(a.customers[1])
<__main__.Person object at 0x105712ef0>



class Person:
...     def __init__(self, id, first_name, last_name):
...         self.id = id
...         self.first_name = first_name
...         self.last_name = last_name
...     
...     def __str__(self):
...         return f"{self.id} identifies as {self.first_name}_{self.last_name}"
...     



class Person:
...     def __init__(self, id, first_name, last_name):
...         self.id = id
...         self.first_name = first_name
...         self.last_name = last_name
...     
...     def __str__(self):
...         return f"{self.id} identifies as {self.first_name}_{self.last_name}"
... 


James = Person(1, 'James', 'T')
a.customers[1]
<__main__.Person object at 0x105712ef0>
a.customers = []
a.customers
[]
a.add_customer(James)
a.customers[0]
<__main__.Person object at 0x1058ed908>
print(a.customers[0])
1 identifies as James_Thompson


class Person:
...     def __init__(self, id, first_name, last_name):
...         self.id = id
...         self.first_name = first_name
...         self.last_name = last_name
...     
...     def __str__(self):
...         return f"{self.id} identifies as {self.first_name}_{self.last_name}"
...     
...     def __repr__(self):
...         return f"{self.id} identifies as {self.first_name}_{self.last_name}"
...     
Chris = Person(2, 'Chris', 'Chavez')
Chris
2 identifies as Chris_Chavez


class Bank:
...     def __init__(self):
...         self.customers = []
...         self.accounts = []
...     
...     def add_customer(self, customer):
...         print(customer.id)
...         self.customers.append(customer)
...         
zc_bank = Bank()
zc_bank.add_customer(Chris)
2



locals().keys()
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__builtins__', 'sys', 'Bank', 'zc_bank', 'Person', 'James', 'Chris'])
locals().keys()[a]
Traceback (most recent call last):
  File "<input>", line 1, in <module>

locals()[Chris]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 2 identifies as Chris_Chavez
locals()['Chris']
2 identifies as Chris_Chavez


