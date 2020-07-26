# For this challenge, create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

class Account:
    def __init__(self, owner='NOT DEFINED', balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} has deposited successfully!')
    def withdraw(self, amount):
        if int(amount > self.balance):
            print('FAM UR BROKE, ROB A BANK OR SMTH')
        else:
            self.balance = self.balance - amount
            print(f'{amount} has drawn successfully!')
    def __str__(self):
        return(f"Owner's name:\t{self.owner}\nAccount Balance:\t{str(self.balance)}")

myAcc = Account('Ali', 1000)
myAcc.deposit(500)
print(myAcc)
myAcc.withdraw(1500)
print(myAcc)