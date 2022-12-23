class User():
    def __init__(self):
        self.firstname = input("Firstname: ")
        self.surname = input("Surname: ")
        self.age = int(input("Age: "))

    def getDetails(self):
        print(f"{self.firstname} {self.surname} is {self.age} years old")


class Bank(User):
    def __init__(self, user):
        self.user = user
        self.balance = 0

    def deposit(self, amount):
        amount = int(input("How much do you want to deposit?: "))
        self.amount = amount
        self.balance = self.amount + self.balance
        print(f"You have deposited",self.amount, "฿")


    def withdraw(self, amount):
        amount = int(input("How much do you want to withdraw?: "))
        self.amount = amount
        if self.amount > self.balance:
            print("Not enough money")
        else:
            self.balance = self.balance - self.amount
            print(f"You have withdrawn",self.amount, "฿")
            print("Your balance is", self.balance, "฿")

    # def getBalance(self):
    #     self.getDetails()
    #     print("Your balance is " + self.balance + " ฿")

