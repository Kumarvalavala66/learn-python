import random

print("guss the number from 1-100\n to know answer type 1111")
while True:
    number = random.randint(1, 100)

    choice = int(input("enter your choice: "))
    if choice == 1111:
        print(number)
        break

    elif choice>100 or choice<1:
        print('invalid input\n please enter an valid input  ')
    elif choice >number:
        print('the number you entered is too high \n please try again ')
    elif choice <number:

        print('the number you entered is too low \n please try again')
    elif choice == number:
        print('yo you gussed it right :)')
        break


    else:
        print('invalid input\n please enter an valid input  ')
