from bank import User, Bank

def main():
    user = User()
    user.getDetails()
    if user.getDetails():
        bank = Bank(user)
        bank.deposit(amount=0)
        bank.withdraw(amount=0)
        bank.transfer(reciever=bank, amount=0)
    elif user.getDetails() == False:
        print("Thank you for using our bank")


if __name__ == "__main__":
    main()
