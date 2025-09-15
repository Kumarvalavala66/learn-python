import random
my_history = []

while True:

        choice = str(input('want to roll the dice ?  (y/n/h):')).lower()

        if choice == 'y':
            roll = random.randint(1, 6)
            roll1 = random.randint(1, 6)
            my_history.append(roll)
            my_history.append(roll1)
            print(f'({roll} {roll1})')
        elif choice == 'n':
            print('thanks for playing (:')
            break
        elif choice == 'h':
            if my_history!=():
              print(my_history)
            else:
                print('no history to show')
        else:
            print('invalid input\n please enter an valid input  ):')







