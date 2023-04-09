class User:
    def __init__(self, firstName, balance):
        self.firstName=firstName
        self.balance=balance
    def displayUserBalance(self):
        print(f"User:{self.firstName} Balance:{self.balance}")
        return self
    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self.balance
        


oliver=User('oliver', 500)
oliver.displayUserBalance()
oliver.makeWithdrawal(20)
print(oliver.balance)

        