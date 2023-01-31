# This line defines the Tic Tac Toe board as a list of 9 spaces, each initialized as an empty string
board = [' ' for x in range(9)]

def print_board():
    """Print the current state of the Tic Tac Toe board.

    This function takes the current state of the Tic Tac Toe board, represented as a list of 9 spaces, and 
    formats it into a 3x3 grid to display it to the user. The format used here is a series of strings, each 
    representing a row in the Tic Tac Toe board, using the '|' symbol to separate the spaces in each row.
    """
    # The first row is created by taking the values at indices 0, 1, and 2 in the board list and inserting them
    # into the string 'row1', which is formatted as a single row in the Tic Tac Toe board.
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    # The second row is created in the same way, using the values at indices 3, 4, and 5 in the board list.
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    # The third row is created in the same way, using the values at indices 6, 7, and 8 in the board list.
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    # The Tic Tac Toe board is printed with a blank line before and after it for aesthetics.
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon, player_type):
    """Make a move on the Tic Tac Toe board.

    Args:
        icon (str): The player's symbol ('X' or 'O').
        player_type (str): The type of player (either 'human' or 'computer').
    """
    if player_type == 'human':
        if icon == 'X':
            number = 1
        elif icon == 'O':
            number = 2

        print("Your turn player {}".format(number))
        while True:
            choice = int(input("Enter your move (1-9): ").strip())
            # If the space the player selected is currently unoccupied, update the board to reflect their move.
            if board[choice - 1] == ' ':
                board[choice - 1] = icon
                break
            # If the space the player selected is already occupied, prompt the player to select another space.
            else:
                print("\nThat space is already taken! Please select another space.")
    else:
        # hey future me PAY ATTENTION, Code for the computer's move goes here, quit being lazy and study mini-max algorithm for a change
        # Tic toc toe is a mathematically solved game so this shouldn't be too difficult
        # famous last words
        pass

def is_victory(icon):
    """
    Check if the current player with the specified icon has won the game.

    Args:
    - icon (str): The player's symbol ('X' or 'O').

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    # Check for victory conditions for all rows
    for i in range(3):
        if board[3*i] == icon and board[3*i + 1] == icon and board[3*i + 2] == icon:
            return True
    # Check for victory conditions for all columns
    for i in range(3):
        if board[i] == icon and board[i + 3] == icon and board[i + 6] == icon:
            return True
    # Check for victory conditions for the two diagonals
    if board[0] == icon and board[4] == icon and board[8] == icon:
        return True
    if board[2] == icon and board[4] == icon and board[6] == icon:
        return True
    # If none of the victory conditions have been met, the game is not won yet
    return False

def is_draw():
    """
    Check if the game has ended in a draw.

    Returns:
    - bool: True if the game has ended in a draw, False otherwise.
    """
    # If there are no spaces left on the board that are still unoccupied, the game is a draw
    return ' ' not in board

while True:
    # Print the current state of the board
    print_board()

    # Get the move from player 1 (X)
    player_move('X', 'human')
    # Check if player 1 has won the game
    if is_victory('X'):
        print("\nX wins! Congratulations!")
        break
    # Check if the game has ended in a draw
    elif is_draw():
        print("\nIt's a draw!")
        break

    # Print the current state of the board
    print_board()

    # Get the move from player 2 (O)
    player_move('O', 'human')
    # Check if player 2 has won the game
    if is_victory('O'):
        print_board()
        print("\nO wins! Congratulations!")
        break
    # Check if the game has ended in a draw
    elif is_draw():
        print("\nIt's a draw!")
        break