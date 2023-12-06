"""
Connect 4 Game - Assignment 2 Software Development
"""

def create_board(rows, columns) -> list:
    """
    This function creates the game board with the given number of rows and columns.

    Returns:
        list: A 2D list representing the game board.
    """
    return [[' ' for _ in range(columns)] for _ in range(rows)]

def display_board(board):
    """
    This function displays the game board.

    Args:
        board (list): A 2D list representing the game board.
    """
    for row in board:
        print('|'.join(row))

    board_width = len(board[0])

    print('—' * (board_width * 2 - 1))

    for col in range(1, board_width + 1):
        print(f' {col}', end='')

    print()

def get_player_names():
    """
    Prompt the user to enter the names of the two players.

    Returns:
        tuple: A tuple containing the names of the two players.
    """
    player1 = input("Player 1, enter your username (max 2 characters)\n> ")
    player2 = input("Player 2, enter your username (max 2 characters)\n> ")
    return player1, player2

def is_board_full(board):
    """
    Simply checks if the game board is full.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(' ' not in row for row in board)

def get_column_choice(player, max_column_range):
    """
    Prompt the player to choose a column.

    Args:
        player (str): The name of the player.

    Returns:
        int: The chosen column index.
    """
    while True:
        try:
            column = int(input(f"{player}, choose a column: ")) - 1
            if 0 <= column <= max_column_range:
                break
            print(f"Please choose a column between 1 and {max_column_range + 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return column

def valid_move(column, board):
    """
    Checks if a move is a valid one.

    Args:
        column (int): The index of the column to place a piece.
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    column_in_board = 0 <= column < len(board[0])
    chosen_row_empty = board[0][column] == ' '

    return column_in_board and chosen_row_empty

def place_piece(column, current_player, board):
    """
    Places a piece in the specified column.

    Args:
        column (int): The index of the column to place a piece.
        current_player (str): The name of the current player.
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the piece is successfully placed, False otherwise.
    """
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = current_player
            return True  # Return True when a piece is successfully placed
    return False  # Return False if the column is already full

def check_win_condition(board):
    """
    Check if there is a win condition in the game.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if there is a win condition, False otherwise.
    """
    # Check rows for a win
    for row, _ in enumerate(board):
        for col in range(len(board[0]) - 3):
            if (
                board[row][col]     ==
                board[row][col + 1] ==
                board[row][col + 2] ==
                board[row][col + 3] != ' '
            ):
                return True

    # Check columns for a win
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if (
                board[row][col]     ==
                board[row + 1][col] ==
                board[row + 2][col] ==
                board[row + 3][col] != ' '
            ):
                return True

    # Check diagonals (top-left to bottom-right) for a win
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if (
                board[row][col]         ==
                board[row + 1][col + 1] ==
                board[row + 2][col + 2] ==
                board[row + 3][col + 3] != ' '
            ):
                return True

    # Check diagonals (bottom-left to top-right) for a win
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if (
                board[row][col]         ==
                board[row - 1][col + 1] ==
                board[row - 2][col + 2] ==
                board[row - 3][col + 3] != ' '
            ):
                return True

    return False  # Return False if no win condition is met

def switch_players(current_player, player1, player2):
    """
    Switch the current player.

    Args:
        current_player (str): The name of the current player.
        player1 (str): The name of the first player.
        player2 (str): The name of the second player.

    Returns:
        str: The name of the next player.
    """
    if current_player == player1:
        return player2
    else:
        return player1

def get_board_dimensions(min_rows, max_rows, min_cols, max_cols):
    """
    Get the dimensions of the game board through user input.

    Args:
        min_rows (int): The minimum number of rows.
        max_rows (int): The maximum number of rows.
        min_cols (int): The minimum number of columns.
        max_cols (int): The maximum number of columns.
    Returns:
        tuple: A tuple containing the number of rows and columns.
    """

    rows = input(f"Please select how many rows you want (min {min_rows}, max {max_rows})\n> ")
    cols = input(f"Please select how many columns you want (min {min_cols}, max {max_cols})\n> ")

    return int(rows), int(cols)

# Main game loop
def main():
    """
    The main entry point and game loop.
    """
    player1, player2 = get_player_names()
    rows, cols = get_board_dimensions(8, 18, 6, 12)

    board = create_board(rows, cols)

    current_player = player1

    WIN_MESSAGE = f"{current_player} wins!"
    DRAW_MESSAGE = f"It's a draw between {player1} and {player2}!"
    INVALID_MOVE_MESSAGE = "That wasn't a valid move. Please try again."

    print(f"Welcome to the game, {player1} and {player2}!")

    while True:
        display_board(board)

        while not check_win_condition(board) and not is_board_full(board):
            if not any(player1 in row or player2 in row for row in board):  # Check if it's the first turn
                current_player = player1
            else:
                current_player = switch_players(current_player, player1, player2)
            column = get_column_choice(current_player, cols - 1)

            if valid_move(column, board):
                place_successful = place_piece(column, current_player, board)
                if place_successful:
                    display_board(board)
                    if check_win_condition(board):
                        print(WIN_MESSAGE)
                    if is_board_full(board):
                        print(DRAW_MESSAGE)
                else:
                    print(INVALID_MOVE_MESSAGE)
            else:
                print(INVALID_MOVE_MESSAGE)

        restart_option = input("Want to play again? (y/n) ")
        if restart_option.lower() == "y":
            board = create_board(rows, cols)
            current_player = player1
        else:
            break


if __name__ == "__main__":
    main()
