# import random
#
# grid = ["1","2","3","4","5","6","7","8","9"]
# choices = ["A","B","C"]
#
# MAX_ROWS= 3
# MAX_COLN = 3
# min_deposite = 100
# min_bet = 1
# remaining_amount = 0
# # Asking user about deposit
# # print("\nWelcome to Gambling!\n")
# def user_details():
#     while True:
#           deposit = int(input("Enter the amount to deposite :₹"))
#           if deposit <= min_deposite:
#               print("\nYour deposit is is lower than the minimum deposite.")
#               continue
#           else:
#               break
#     return deposit
#
#
# # showing the lines
# def display(grid):
#     for i in range(MAX_ROWS):
#         min__ = i*3
#         max__ = (i+1)*3
#         print("|".join(grid[min__:max__]))
#
#
# # gettiing random selection from computer
# def random_selection():
#     for i in range(9):
#         computer_choice = random.choice(choices)
#         grid[i] = computer_choice
#     return grid
#
# # checking the about won by user
# def winning_game(bet):
#     winning_amount = 0
#     streak = 0
#     winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#     for rows in range(MAX_ROWS):
#         for i, j, k in winning_combinations:
#             if grid[i] == grid[j] == grid[k]:
#                 streak += 1
#             else:
#                 pass
#
#     if streak == 3:
#         winning_amount = bet * 6
#         print(f"you win! {winning_amount})")
#     elif streak == 2:
#         winning_amount = bet * 4
#         print(f"you win! {winning_amount})")
#     elif streak == 1:
#         winning_amount = bet * 2
#         print(f"you win! {winning_amount})")
#     elif streak == 0:
#         print(f"you lost ")
#         winning_amount = 0
#     return winning_amount
#
#
#
#
# def asking_for_bet(deposit):
#     # bet = int(input("enter the anount you want to bet: ₹"))
#     global remining_amount
#     while True:
#      bet = int(input("enter the anount you want to bet: ₹"))
#      if bet <= min_bet or  bet >= deposit:
#          print("\nSorry, your bet can't be placed!")
#          continue
#      else:
#          remining_amount = deposit - bet
#          break
#     return bet, remining_amount
#
#
# def play_game():
#     # asking_for_play = str(input("Do you want to play again? (Y/N) : ")).lower()
#     # if asking_for_play == "y":
#     deposit = user_details()
#     rows = [1,2,3]
#     while True:
#         asking_for_play = str(input("Do you want to play again? (Y/N) : ")).lower()
#         if asking_for_play == "y":
#             print(f"your available amount {deposit}")
#             bet_amount, re_amount = asking_for_bet(deposit)
#             deposit -= bet_amount
#             print(f"your available amount {deposit}")
#             allo = random_selection()
#             display(allo)
#             winning_amount = winning_game(allo)
#             deposit = deposit + winning_amount
#             print(f"your total amount {deposit-bet_amount+winning_amount}")
#         elif asking_for_play == "n":
#             print("Thank you for playing!")
#             break
#
# play_game()
import random

choices = ["A", "B", "C"]
MAX_ROWS = 3
MAX_COLS = 3
MIN_DEPOSIT = 100
MIN_BET = 1


def user_details():
    """Prompts the user for a valid deposit amount."""
    while True:
        try:
            deposit = int(input(f"Enter the amount to deposit (minimum {MIN_DEPOSIT}): "))
            if deposit < MIN_DEPOSIT:
                print("Your deposit is lower than the minimum deposit. Please try again.")
            else:
                return deposit
        except ValueError:
            print("Invalid input. Please enter a number.")


def display(grid):
    """Displays the 3x3 slot machine grid."""
    for i in range(MAX_ROWS):
        min_idx = i * MAX_COLS
        max_idx = (i + 1) * MAX_COLS
        print("|".join(grid[min_idx:max_idx]))


def random_selection():
    """Generates and returns a new random grid for the slot machine."""
    return [random.choice(choices) for _ in range(MAX_ROWS * MAX_COLS)]


def check_winnings(grid, bet):
    """
    Checks for winning rows and calculates the winning amount.
    Returns the payout.
    """
    winning_amount = 0
    num_winning_lines = 0

    # Define the winning row combinations
    winning_combinations = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8)  # Third row
    ]

    for i, j, k in winning_combinations:
        if grid[i] == grid[j] == grid[k]:
            num_winning_lines += 1

    if num_winning_lines == 3:
        winning_amount = bet * 6
        print(f"Jackpot! You won {winning_amount} for 3 winning lines!")
    elif num_winning_lines == 2:
        winning_amount = bet * 4
        print(f"You won {winning_amount} for 2 winning lines!")
    elif num_winning_lines == 1:
        winning_amount = bet * 2
        print(f"You won {winning_amount} for 1 winning line!")
    else:
        print(f"You lost this round.")

    return winning_amount


def ask_for_bet(balance):
    """Prompts the user for a valid bet amount."""
    while True:
        try:
            bet = int(input("Enter the amount you want to bet: "))
            if bet < MIN_BET:
                print("Your bet must be greater than the minimum bet.")
            elif bet > balance:
                print(f"You don't have enough funds. Your current balance is {balance}.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    """Manages the main game loop."""
    balance = user_details()

    while True:
        if balance <= 0:
            print("You have run out of funds. Game over!")
            break

        print(f"\nYour current balance: {balance}")

        while True:
            asking_for_play = input("Do you want to play? (Y/N): ").lower()
            if asking_for_play == "y":
                break
            elif asking_for_play == "n":
                print(f"Thank you for playing! Your final balance is {balance}.")
                return
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        bet_amount = ask_for_bet(balance)
        balance -= bet_amount

        slot_grid = random_selection()
        display(slot_grid)

        winnings = check_winnings(slot_grid, bet_amount)
        balance += winnings

        print(f"Your new balance is {balance}.")


if __name__ == "__main__":
    play_game()
