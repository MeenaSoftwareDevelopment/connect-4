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

def get_column_choice(player):
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
            if 0 <= column <= 11:
                break
            print("Please choose a column between 1 and 11.")
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
    def check_direction(row, col, row_offset, col_offset):
        """
        Check for a win in the specified direction.

        Args:
            row (int): Starting row index.
            col (int): Starting column index.
            row_offset (int): The number of rows to move in the specified direction.
            col_offset (int): The number of columns to move in the specified direction.

        Returns:
            bool: True if there is a win condition in the specified direction, False otherwise.
        """
        for i in range(3):
            if board[row][col] != board[row + row_offset * i][col + col_offset * i] != ' ':
                return False
        return True

    # Check rows for a win
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if check_direction(row, col, 0, 1):
                return True

    # Check columns for a win
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if check_direction(row, col, 1, 0):
                return True

    # Check diagonals (top-left to bottom-right) for a win
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if check_direction(row, col, 1, 1):
                return True

    # Check diagonals (bottom-left to top-right) for a win
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if check_direction(row, col, -1, 1):
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

def display_winner(player):
    """
    Simply displays the name of the winner.

    Args:
        player (str): The name of the winner.
    """
    print(f"Player {player} wins!")

# Main game loop
def main():
    """
    The main entry point and game loop.
    """
    player1, player2 = get_player_names()
    game_over = False
    ROWS = int(input("Please select how many rows you want (Minimum of 8, Maximum of 18): "))  # Define the number of rows
    COLS = int(input("Please select how many columns you want (Minimum of 6, Maximum of 12): "))  # Define the number of columns
    board = create_board(ROWS, COLS)  # Initialize the game board

    current_player = player1  # Initializing current_player here

    while not game_over:
        display_board(board)

        while not is_board_full(board):
            current_player = switch_players(current_player, player1, player2)  # Pass the necessary arguments
            column = get_column_choice(current_player)

            if valid_move(column, board):  # Pass the 'board' argument to valid_move
                place_successful = place_piece(column, current_player, board)  # Pass the 'board' argument to place_piece
                if place_successful:
                    if check_win_condition(board):  # Pass the 'board' argument to check_win_condition
                        game_over = True
                        display_board(board)
                        display_winner(current_player)
                    elif is_board_full(board):
                        game_over = True
                        display_board(board)
                        display_draw_message()
                else:
                    display_invalid_move_message()
            else:
                display_invalid_move_message()

        # Game Over State
        restart_option = input("Press 'r' to restart or any other key to quit: ")
        if restart_option.lower() == "r":
            board = create_board(ROWS, COLUMNS)
            game_over = False
            current_player = player1
        else:
            quit()

if __name__ == "__main__":
    main()
