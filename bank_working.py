#     Create a class BankAccount with methods deposit, withdraw, and check_balance.

class BankAccount :
    def __init__(self, name,id, balance):
        self.name = name
        self.id = id
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount} into {self.id}")


    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name} withdrawed {amount} into {self.id}")


    def print_balance(self):
        print(f"{self.name} balance: {self.balance}")




print("-------------------->WLLCOME TO SOME BANK <-----------------------------")


def user_detail():
    while True:
        try:
            name = input("Enter your name: ")
            id = int(input("Enter your id: "))
            amount = int(input("Enter your amount: "))
            user1 = BankAccount(name, id, amount)
            break
            return user1
        except ValueError:
            print("Invalid input. Please try again.")
            continue

def deposit(user):
    amount = int(input("Enter your amount: "))
    user.deposit(amount)
    print("Deposited successfully!")
    return user
def withdraw(user):
    with_amount = int(input("Enter your amount: "))
    print("You cannot withdraw negative amount." if with_amount < 0 or with_amount > user.balance else user.withdraw(with_amount))
    return user
def print_balance(user):
    print(f"{user.name} balance: {user.balance}")

    def bank():
        user_input = input("Want to hop in the bank? (y/n): ").lower().strip()
        if user_input == "n":
            print("Bye!")
            return

        user = user_detail()

        option_for_user = input("Enter your option (d=deposit, w=withdraw, b=balance): ").lower().strip()
        match option_for_user:
            case "d":
                deposit(user)
            case "w":
                withdraw(user)
            case "b":
                print_balance(user)
            case _:
                print("Invalid input. Please try again.")


