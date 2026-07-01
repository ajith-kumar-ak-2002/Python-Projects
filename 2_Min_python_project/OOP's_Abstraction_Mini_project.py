### By Using Abstraction Project

from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance (self,amount):
        pass

# Concrete Amount

class SBI_ATM(ATM):
    def __init__(self , balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Amount: {self.balance}")
        else:
            print("Insuffient Balance!")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Current: {self.balance}")

    def check_balance(self):
       print(f"Checking balance; {self.balance}")


#using Abstraction

user1 = SBI_ATM(5000)

user1.check_balance()
user1.withdraw(2000)
user1.deposit(1000)
user1.check_balance()