# Write a program to demonstrate Encapsulated Banking System with Inheritance Models.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(self.name, "Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Savings Account Transaction")
        super().withdraw(amount)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Current Account Transaction")
        if amount <= self.get_balance() + 2000 and amount > 0:
            balance = self.get_balance()

            if amount <= balance:
                super().withdraw(amount)
            else:
                super().withdraw(balance)
                print("Overdraft used:", amount - balance)
                print("Overdraft debt:", amount - balance)
        else:
            print("Overdraft limit exceeded")


# Create account objects
s1 = SavingsAccount("Annu", 10000)
c1 = CurrentAccount("Riya", 5000)

# Polymorphism: same method, different account objects
accounts = [s1, c1]

for account in accounts:
    account.withdraw(6000)
    account.display()
    print()