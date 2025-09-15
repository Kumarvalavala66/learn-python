# import random
# # ask usernames
# # give turn to first player
# # loop for rolling dice until one
# #if one score will be zero
# #loop for second player
# #any one reaches 25 wins
# print("Welcome to Pig Game!")
# while True:
#     player1 = input("Enter your name of player 1: ")
#     player2 = input("Enter your name of player 2: ")
#     if player1 == '' or player2 == '':
#         print("Please enter your names first!")
#         continue
#     if player1 == player2:
#         print("no same name")
#         continue
#     else:
#         break
#
# main_score_player1 = 0
# main_score_player2 = 0
# turn = 0
# def player1_playing():
#     global main_score_player1
#     global turn
#     score1 = 0
#     temp = main_score_player1
#     while turn == 0:
#         user_choice_play =str(input(f'{player1} do you want to roll dice (y/n)')).lower()
#         if  user_choice_play == 'y':
#             dice1 = random.randint(1, 6)
#             print(f'{player1} rolled a {dice1}')
#             if dice1 == 1:
#                 print(f"you lost {score1}")
#                 print(f"{player1} total score is {temp}")
#                 turn = 1
#                 return turn,temp
#             else:
#                 score1+=dice1
#                 print("your score is:", score1)
#                 main_score_player1 += dice1
#                 print( player1 +" total score is:",main_score_player1)
#                 continue
#         elif user_choice_play == 'n':
#             print(f'your total score is {main_score_player1}')
#             turn = 1
#             return  main_score_player1
#         else:
#             print("please enter y or n")
#             continue
#
# def player2_playing():
#     global main_score_player2
#     global turn
#     score2 = 0
#     temp2 = main_score_player2
#     while turn == 1:
#         user_choice_play =str(input(f'{player2} do you want to roll dice (y/n)')).lower()
#         if  user_choice_play == 'y':
#             dice2 = random.randint(1, 6)
#             print(f'{player2} rolled a {dice2}')
#             if dice2 == 1:
#                 print(f"you lost {score2}")
#                 print(f"{player2} total score is {temp2}")
#                 turn = 0
#                 return turn,temp2
#             else:
#                 score2+=dice2
#                 print("your score is:", score2)
#                 main_score_player2 += dice2
#                 print( player2+"total score is:", main_score_player2)
#                 continue
#         elif user_choice_play == 'n':
#             print(f'{player2} total score is {main_score_player2}')
#             turn = 0
#             return turn , main_score_player2
#         else:
#             print("please enter y or n")
#             continue
#
#
# def check_win():
#     result1 = player1_playing()
#     result2 = player2_playing()
#
#
#     if result1 >= 100:
#         winner = player1
#         return winner
#
#
#     elif result2 >= 100:
#         winner2 = player2
#         return winner2
#     else:
#         return None
#
#
#
#
#
#
#
#
# def playing():
#     while True:
#         player1_playing()
#         check_win()
#         winner = check_win()
#         if winner == player1:
#             print(f"{player1} wins!")
#             break
#         player2_playing()
#         check_win()
#         winner = check_win()
#         if winner == player2:
#             print(f"{player2} wins!")
#             break
#         if winner == None:
#             continue
#
# playing()
#
import random

print("🎲 Welcome to Pig Game! First to reach 25 points wins 🎉")

# Get player names
while True:
    player1 = input("Enter name of Player 1: ").strip()
    player2 = input("Enter name of Player 2: ").strip()

    if not player1 or not player2:
        print("❌ Please enter both names!")
        continue
    if player1 == player2:
        print("❌ Players cannot have the same name!")
        continue
    break

# Scores
main_score_player1 = 0
main_score_player2 = 0
turn = 0   # 0 = Player1, 1 = Player2
TARGET = 25

def player_turn(player, score):
    """Handles one player's turn"""
    temp_score = 0
    global turn

    while True:
        choice = input(f"{player}, do you want to roll dice? (y/n): ").lower()
        if choice == "y":
            dice = random.randint(1, 6)
            print(f"🎲 {player} rolled a {dice}")

            if dice == 1:
                print(f"❌ {player} loses all turn points!")
                return score  # no score added
            else:
                temp_score += dice
                print(f"👉 Turncore = {temp_score}, Total if held = {score + temp_score}")
        elif choice == "n":
            score += temp_score
            print(f"✅ {player}'s total score = {score}")
            return score
        else:
            print("Please enter 'y' or 'n'.")

def check_winner(score, player):
    if score >= TARGET:
        print(f"🎉 {player} wins with {score} points!")
        return True
    return False

# Main game loop
while True:
    if turn == 0:
        main_score_player1 = player_turn(player1, main_score_player1)
        if check_winner(main_score_player1, player1):
            break
        turn = 1
    else:
        main_score_player2 = player_turn(player2, main_score_player2)
        if check_winner(main_score_player2, player2):
            break
        turn = 0