import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
      for col in row:
        if col == 'X':
          x_count += 1
        elif col == 'O':
            o_count += 1
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = []
    for row in board:
      new_row = row[:]
      new_board.append(new_row)
    new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    if board[0][0] == board[0][1] and board[0][2]==board[0][0]:
            return board[0][0]
    elif board[1][0] == board[1][1] and board[1][2]==board[1][0]:
      return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0]==board[2][2]:
      return board[2][0]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_turn = player(board)
    
    if player_turn == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            new_score = int(min_value(result(board, action)))
            if new_score > best_score:
                best_score = new_score
                best_move = action
    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            new_score = int(max_value(result(board, action)))
            if new_score < best_score:
                best_score = new_score
                best_move = action

    return best_move


def max_value(board):
    if terminal(board):
        return utility
# from tic_tac_toe import *

def play_game():
    # Initialize the game board
    board = initial_state()

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not terminal(board):
        # Get the current player
        current_player = player(board)

        # Ask the current player for their move
        print(f"Player {current_player}, it's your turn.")
        i = int(input("Enter the row number (0-2): "))
        j = int(input("Enter the column number (0-2): "))
        action = (i, j)

        # Check if the move is valid
        if action not in actions(board):
            print("Invalid move. Try again.")
            continue

        # Update the game board
        board = result(board, action)

        # Print the updated board
        print_board(board)

    # Check for the winner
    game_winner = winner(board)
    if game_winner is None:
        print("The game ended in a tie.")
    else:
        print(f"Player {game_winner} won the game!")

def print_board(board):
    """
    Prints the current state of the board.
    """
    print("-------------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            if cell is None:
                print(" ", end=" | ")
            else:
                print(cell, end=" | ")
        print()
        print("-------------------")

if __name__ == '__main__':
    play_game()
