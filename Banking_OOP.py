#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print("Personal Details")
        print("")
        print(f"Name {self.name}")
        print(f"Age {self.age}")
        print(f"Gender {self.gender}")

#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Account balance has been updated: ${self.balance}")

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient Funds | Balance Available ${self.balance} ")
        else:
            self.balance = self.balance - self.amount
            print(f"Account balance updated: ${self.balance}")

    def view_balance(self):
        self.show_info()
        print(f"Account balance: ${self.balance}")

rowan = Bank('Rowan',19,'Male')
rowan.deposit(1000)
rowan.withdraw(680)
rowan.view_balance()