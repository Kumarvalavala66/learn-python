LENGTH = 3

# Get player names
player1 = input('Enter your player1: ')
player2 = input('Enter your player2: ')
user_play = input(f"Hello {player1} & {player2}, do you want to play the game? (y/n) ").lower()

# Initial board and player options
total_elements = ['1','2','3','4','5','6','7','8','9']
user_options = ("x","o")


def select_user_details():
    while True:
        player1_selection = input(f'{player1}, select a symbol (X/O): ').lower()
        player2_selection = input(f'{player2}, select a symbol (X/O): ').lower()

        if (player1_selection not in user_options) or (player2_selection not in user_options):
            print("Invalid input! Choose X or O.")
            continue
        elif player1_selection == player2_selection:
            print("Both players cannot choose the same symbol!")
            continue
        else:
            print(f"{player1} selected {player1_selection}")
            print(f"{player2} selected {player2_selection}")
            return player1_selection, player2_selection


def display_board():
    for i in range(LENGTH):
        slice_start = i * 3
        slice_end = (i + 1) * 3
        print(" | ".join(total_elements[slice_start:slice_end]))
    print()  # extra line for spacing


def check_win():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a,b,c in win_patterns:
        if total_elements[a] == total_elements[b] == total_elements[c]:
            if total_elements[a] in ('x','o'):
                return total_elements[a]  # winner symbol
    return None  # no winner yet


def play():
    player1_selection, player2_selection = select_user_details()
    display_board()

    turn = 0  # 0 for player1, 1 for player2

    while True:
        if turn == 0:
            current_player = player1
            symbol = player1_selection
        else:
            current_player = player2
            symbol = player2_selection

        move = input(f"{current_player}, select a place to place {symbol} (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        index = int(move) - 1

        if total_elements[index] in ('x','o'):
            print("Spot already taken! Choose another spot.")
            continue

        # Place symbol
        total_elements[index] = symbol
        display_board()

        # Check win
        winner = check_win()
        if winner:
            print(f"{current_player} wins! 🎉")
            break

        # Check draw
        if all(cell in ('x','o') for cell in total_elements):
            print("It's a draw! 🤝")
            break

        # Switch turn
        turn = 1 - turn


if user_play == 'y':
    play()
else:
    print("Game exited. See you next time!")