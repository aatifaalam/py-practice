class ATM:
     def __init__(self, name, balance):
              self.name = name
              self.balance = balance
     def deposit(self, amount):
           self.balance = self.balance + amount
     def withdraw(self, amount):
           self.balance = self.balance - amount
     def show_balance(self):
           print(self.name, "Balance: " , self.balance)

a = ATM("Aatif",1000)
a.deposit(500)
a.withdraw(200)
a.show_balance()