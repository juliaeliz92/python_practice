#Create a class representing a simple bank account with deposit and withdraw methods
class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance:
            self.balance = self.balance - amount

    def get_balance(self):
        print(self.balance)

bank1 = Bank(1000)
bank1.get_balance()
bank1.withdraw(50)
bank1.get_balance()
bank1.deposit(200)
bank1.get_balance()