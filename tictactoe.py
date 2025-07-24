print("Hello, welcome to Tic Tac Toe!")
print("This is a two-player game where you can play against a friend.")
print("The board positions are numbered from 1 to 9 as follows:")       

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column 1-3, e.g. 1 3): ")
            row, col = map(int, move.split())
            if board[row - 1][col - 1] not in ['X', 'O']:
                return row - 1, col - 1
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Use row and column numbers between 1 and 3.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        elif is_draw(board):
            print("It's a draw! 🤝")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
