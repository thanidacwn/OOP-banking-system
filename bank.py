import pandas as pd

class User():
    def __init__(self):
        self.firstname = input("Firstname: ")
        self.surname = input("Surname: ")

    def getDetails(self):
        self.age = int(input("Age: "))
        if self.age < int(15):
            raise ValueError("You are too young to use our bank")
        self.gender = input("Gender(Male or Female):")
        if self.gender == "Male":
            print(f"Welcome Mr.{self.firstname} {self.surname} :)")
        elif self.gender == "Female":
            print(f"Welcome Mrs.{self.firstname} {self.surname} :)")
        else:
            raise ValueError("Invalid input")


class Bank(User):
    def __init__(self, user):
        self.user = user
        self.balance = 0

    def deposit(self, amount):
        amount = int(input("How much do you want to deposit?: "))
        self.amount = amount
        self.balance = self.amount + self.balance
        print(f"You have deposited",self.amount, "฿")
        menu = input("What do you want to do next?(deposit, withdraw, transfer, Nothing): ")
        if menu == "deposit":
            self.deposit(amount)
        if menu == "withdraw":
            self.withdraw(amount)
        if menu == "transfer":
            self.transfer(reciever=Bank, amount=0)
        else:
            print("Thank you for using our bank")


    def withdraw(self, amount):
        amount = int(input("How much do you want to withdraw?: "))
        self.amount = amount
        if self.amount > self.balance:
            print("Not enough money to withdraw")
        else:
            self.balance = self.balance - self.amount
            print(f"You have withdrawn",self.amount, "฿")
            print("Now, Your balance is", self.balance, "฿")

    def transfer(self, reciever, amount):
        reciever = "Bhayu"
        print(reciever)
        self.reciever_firstname = input("Who do you want to transfer to?(reciever-firstname): ")
        if reciever == self.reciever_firstname:
            amount = int(input("How much do you want to transfer?: "))
            self.amount = amount
            if self.amount > self.balance:
                print("Not enough money to transfer")
                print("Now, Your balance is", self.balance, "฿")
            else:
                amount.withdraw(amount)
                self.deposit(amount)
                reciever.deposit(amount)
                self.balance = self.balance - self.amount
                print(f"You have transferred",self.amount, "฿")
                print("Now, Your balance is", self.balance, "฿")
        else:
            print("No such user, You can not transfer money to this user")
    
    # def getBalance(self):
    #     self.getDetails()
    #     print("Your balance is " + self.balance + " ฿")

