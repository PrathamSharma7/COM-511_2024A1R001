'''
Create a BankAccount class that stores an account holder's name and balance. Add instance method
to deposit money, withdraw money and display balance. DO NOT ALLOW WITHDRAWAL GREATER THAN AVAILABLE BALANCE
'''

class BankAccount:
    def __init__(self, n, b):
        self.account_holder_name = n
        self.balance = b

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return
        print("INSUFFICIENT BALANCE")

    def display_balance(self):
        print("Balance:", self.balance)

acc1 = BankAccount("John", 1000)
acc1.deposit(500)
acc1.withdraw(2000)
acc1.display_balance()
acc1.withdraw(1000)
acc1.display_balance()