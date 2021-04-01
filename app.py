# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


# Child class


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Account balance is updated: {self.balance}")

    def withdraw(self, amount):
        if(self.balance > 0 and self.balance - amount >= 0):
            self.balance -= amount
            print(f'money withdrawn, new balance: {self.balance}')
        else:
            print(f'Your balance not enough, current balance: {self.balance}')

    def show_balance(self):
        print(f'current balance : {self.balance}')
