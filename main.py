from bank import User, Bank

def main():
    user = User()
    bank = Bank(user)
    print("Welcome to the bank")
    user.getDetails()
    bank.deposit(amount=0)
    bank.withdraw(amount=0)

if __name__ == "__main__":
    main()
