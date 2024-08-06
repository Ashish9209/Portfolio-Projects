Let’s break down the Tic-tac-toe code piece by piece:

### Functions

1. **`initialize_board()`**
   ```python
   def initialize_board():
       """Initialize a 3x3 board."""
       return [[' ' for _ in range(3)] for _ in range(3)]
   ```
   - **Purpose**: Creates and returns a new 3x3 game board.
   - **Details**: 
     - Uses a nested list comprehension to generate a 3x3 grid.
     - Each cell of the grid is initialized with a space `' '`, indicating it's empty.

2. **`print_board(board)`**
   ```python
   def print_board(board):
       """Print the board."""
       print("  0 1 2")
       for i, row in enumerate(board):
           print(i, ' '.join(row))
   ```
   - **Purpose**: Prints the current state of the game board.
   - **Details**:
     - Prints column indices (0, 1, 2) at the top.
     - Iterates over the rows of the board, printing each row with its index (0, 1, 2).
     - `' '.join(row)` converts each row list into a space-separated string.

3. **`check_win(board, player)`**
   ```python
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
   ```
   - **Purpose**: Checks if the given player has won the game.
   - **Details**:
     - Defines all possible win conditions (horizontal, vertical, diagonal).
     - Checks if the current player's symbol (`player`) appears in any of the win conditions.
     - Returns `True` if the player has won, otherwise `False`.

4. **`check_draw(board)`**
   ```python
   def check_draw(board):
       """Check if the board is full and there's no winner."""
       for row in board:
           if ' ' in row:
               return False
       return True
   ```
   - **Purpose**: Checks if the game has ended in a draw.
   - **Details**:
     - Iterates over each row to see if there are any empty spaces (`' '`).
     - Returns `True` if no empty spaces are found (the board is full), and `False` otherwise.

5. **`make_move(board, player, row, col)`**
   ```python
   def make_move(board, player, row, col):
       """Make a move on the board."""
       if board[row][col] == ' ':
           board[row][col] = player
           return True
       else:
           print("Invalid move. The cell is already occupied.")
           return False
   ```
   - **Purpose**: Places the player's symbol on the board at the specified location.
   - **Details**:
     - Checks if the specified cell is empty (`' '`).
     - If empty, updates the board with the player's symbol and returns `True`.
     - If not empty, prints an error message and returns `False`.

### Main Function

6. **`main()`**
   ```python
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
   ```
   - **Purpose**: Manages the game flow and player interactions.
   - **Details**:
     - Initializes the game board and player symbols.
     - Uses a `while` loop to keep the game running until a win or draw is detected.
     - Alternates between players after each valid move.
     - Prompts players to input their move and checks the validity of the move.
     - Calls `make_move()`, `check_win()`, and `check_draw()` to update and evaluate the board.
     - Ends the game with appropriate messages if a player wins or if it's a draw.

7. **`if __name__ == "__main__":`**
   ```python
   if __name__ == "__main__":
       main()
   ```
   - **Purpose**: Ensures that `main()` is called when the script is executed directly.
   - **Details**:
     - This block runs the `main()` function if the script is executed as the main program, not if it is imported as a module.

### Summary

This code implements a simple terminal-based Tic-tac-toe game in Python. It sets up a 3x3 game board, allows two players to take turns making moves, and checks for win or draw conditions after each move. The game continues until one player wins or the board is filled with no winner.