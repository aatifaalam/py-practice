class BankAccount:

    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        if (amount <= 0):
            print("Invalid deposit amount")
            return self.balance

        self.balance = self.balance + amount
        print("Deposited: " + str(amount))
        return self.balance

    def withdraw(self, amount):

        if (amount <= 0):
            print("Invalid withdrawal amount")
            return self.balance

        if (amount > self.balance):
            print("Insufficient balance")
            return self.balance

        # Update balance
        self.balance = self.balance - amount
        print("Withdrawn: " + str(amount))
        return self.balance

    # Display Method
    def displayBalance(self):
        print("Account Holder: " + self.accountHolder)
        print("Current Balance: " + str(self.balance))
        
    
acc = BankAccount("Aatif", 200)
# acc.BankAccount("Aatif", 200)  # This line is unnecessary

acc.displayBalance()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000) 
acc.withdraw(-50)
acc.displayBalance()