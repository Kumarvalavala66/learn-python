	# 7.	Create a function that:
	# •	Tries to convert a string to an integer.
	# •	If it fails, raises a custom exception called InvalidNumberError.
	# •	Always prints "Conversion attempt finished" in finally.


#
class  InvalidNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__("The conversion failed: input is not a number.")

number = str(input("Enter a number: "))
try:
    try:
        number = int(number)
    except ValueError:
        raise InvalidNumberError(number)

except InvalidNumberError as e:
    print(e)
else:
    print(f"{number} is converted to a number.")
finally:
    print("Conversion attempt finished")


	# 8.	Simulate a bank withdrawal system:
	# •	Ask user for withdrawal amount.
	# •	If the amount > balance, raise and handle an error "Insufficient funds".
	# •	If no error, print "Withdrawal successful".
	# •	Always print "Thank you for using our ATM" in finally.

print("------------------->WELCOME TO ATM <--------------------")

class Insufficient_funds(Exception):
    def __init__(self,amount):
        self.amount = amount
        super().__init__("Insufficient funds")


def atm(balance = 10000):
    while True:
        try:
            amount = float(input("Enter amount you want to withdraw : "))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            try:
                if amount > balance:
                    raise Insufficient_funds(amount)
            except Insufficient_funds as e:
                print(e)
                continue
            else:
                balance -= amount
                print(f"Amount {amount} has been withdrawn")
            finally:
                while True:
                    user_choice = input("Do you want to continue? (y/n) : ").lower().strip()
                    match user_choice:
                        case "y":
                          break
                        case "n":
                            print("Thank you for using ATM")
                            return 0
                        case _:
                            print("Please enter y or n")




atm(10000)

