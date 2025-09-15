# import random
#
# player1 =str(input("enter the name of player1  :"))
# player2 = str(input("enter the name of player2  :"))
# dice1=[]
# dice2=[]
# #its for clarifying the choice of player
# x=0
# y=-1
# p1sum=0
# p2sum=0
# a=0
# while True:
#     if x%2==0:
#         ask=str(input(f"{player1} do you want to roll again? (y/n) ")).lower()
#         if ask == 'y':
#             roll = random.randint(-2, 6)
#             print(f'{roll} ')
#             p1sum += roll
#             print(f'{p1sum} ')
#             x=x+1
#             y=y+1
#         elif ask == 'n':
#             print("thanks for playing")
#             break
#
#         if p1sum >=25:
#             a=-1
#             break
#
#     elif y%2==0:
#         ask = str(input(f"{player2} do you want to roll again? (y/n) ")).lower()
#         if ask == 'y':
#             roll = random.randint(-2, 6)
#             print(f'{roll} ')
#             p2sum += roll
#             print(f'{p2sum} ')
#             x=x+1
#             y=y+1
#         elif ask == 'n':
#             print("thanks for playing")
#             break
#
#         if p2sum >=25:
#
#             a=1
#             break
#
#
# if  a==-1:
#     print(f"{player1} wins!")
# elif a==1:
#     print(f"{player2} wins!")
import random

player1 = input("Enter the name of player1: ")
player2 = input("Enter the name of player2: ")

p1sum = 0
p2sum = 0
turn = 1   # 1 = player1's turn, 2 = player2's turn

while True:
    if turn == 1:
        ask = input(f"{player1}, do you want to roll? (y/n) ").lower()
        if ask == 'y':
            roll = random.randint(1, 6)   # normal dice
            print(f"{player1} rolled: {roll}")
            p1sum += roll
            print(f"{player1}'s total = {p1sum}")
            if p1sum >= 25:
                print(f"\n🎉 {player1} wins!")
                break
            turn = 2   # switch to player2
        else:
            print(f"{player1} quits. {player2} wins by default!")
            break
    else:
        ask = input(f"{player2}, do you want to roll? (y/n) ").lower()
        if ask == 'y':
            roll = random.randint(1, 6)
            print(f"{player2} rolled: {roll}")
            p2sum += roll
            print(f"{player2}'s total = {p2sum}")
            if p2sum >= 25:
                print(f"\n🎉 {player2} wins!")
                break
            turn = 1   # switch to player1
        else:
            print(f"{player2} quits. {player1} wins by default!")
            break