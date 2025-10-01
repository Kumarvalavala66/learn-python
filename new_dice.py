import random
my_history = []

while True:

        choice = str(input('want to roll the dice ?  (y/n/h):')).lower()

        if choice == 'y':
            num=int(input('how many dice to roll?'))
            for i in range(num):
                roll = random.randint(1, 6)
                my_history.append(roll)
                print(f'{roll} ')


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







