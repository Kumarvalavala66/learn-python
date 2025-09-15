import random

user_wins = 0
computer_wins = 0
draws = 0
def user_option():
    while True:
        option = str(input('do you want to play again? (y/n)  ')).lower()
        if option == 'y':
            break

        elif option =='n':
            print("thanks for playing")
            break

        else:
            print('invalid input\n please enter an valid input  ')
            continue
    return option

choices = ('r', 'p', 's')
emojis =  {'r':'🪨','p':'📜','s':'✂️'}
while True:
         user_choice = str(input("entr the choice (r/p/s)  :")).lower()
         com_choice = random.choice(choices)
         if user_choice not in choices:
          print('invalid input\n please enter an valid input  ')
          continue
         else:
             print(f'you chose {emojis[user_choice]} \n computer  chose {emojis[com_choice]}')

         if ((user_choice == 'r'and  com_choice =='s') or
            (user_choice == 'p' and com_choice == 'r') or
            (user_choice == 's' and com_choice == 'p')):
            print('you win')
            user_wins += 1
            print(f'you win: {user_wins}\n computer win: {computer_wins} \n draw: {draws}' )
            option = user_option()
            if option == 'y':
                continue
            elif option == 'n':
                break
         elif user_choice ==com_choice :
             print('draw ')
             draws += 1
             print(f'you win: {user_wins}\n computer win: {computer_wins} \n draw: {draws}')
             option = user_option()
             if option == 'y':
                 continue
             elif option == 'n':
                 break
         else:
             print("you lost ")
             computer_wins += 1
             print(f'you win: {user_wins}\n computer win: {computer_wins} \n draw: {draws}')
             option = user_option()
             if option == 'y':
                 continue
             elif option == 'n':
                 break



