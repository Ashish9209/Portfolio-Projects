def initialize_board():
    """Initialize a 3x3 board."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Print the board."""
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, ' '.join(row))

def check_win(board, player):
    """Check if the current player has won."""
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    """Check if the board is full and there's no winner."""
    for row in board:
        if ' ' in row:
            return False
    return True

def make_move(board, player, row, col):
    """Make a move on the board."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Invalid move. The cell is already occupied.")
        return False

def main():
    board = initialize_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]} - Enter row (0, 1, 2): "))
        col = int(input(f"Player {players[current_player]} - Enter column (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3:
            if make_move(board, players[current_player], row, col):
                if check_win(board, players[current_player]):
                    print_board(board)
                    print(f"Player {players[current_player]} wins!")
                    break
                elif check_draw(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                # Switch players
                current_player = 1 - current_player
        else:
            print("Invalid input. Please enter row and column between 0 and 2.")

if __name__ == "__main__":
    main()
