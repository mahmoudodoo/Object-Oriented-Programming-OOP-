
# This is a basic template to start a practical OOP project in Python
# Example: A simple banking system

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Not enough balance")

# Example usage
acc = Account('John Doe', 1000)
acc.deposit(500)
acc.withdraw(200)
