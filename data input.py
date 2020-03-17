
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
    
    