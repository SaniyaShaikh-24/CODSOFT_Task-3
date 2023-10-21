import math

# Constants for representing the players and empty cells
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

# Function to evaluate the board for the AI (using a simple heuristic)
def evaluate(board):
    if check_win(board, PLAYER_X):
        return 10
    elif check_win(board, PLAYER_O):
        return -10
    else:
        return 0

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {
        PLAYER_X: 10,
        PLAYER_O: -10,
        'tie': 0
    }

    if check_win(board, PLAYER_X):
        return scores[PLAYER_X]
    elif check_win(board, PLAYER_O):
        return scores[PLAYER_O]
    elif all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI using Minimax
def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Main game loop
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    player_turn = True  # True for player X, False for player O

    while any(EMPTY in row for row in board) and not check_win(board, PLAYER_X) and not check_win(board, PLAYER_O):
        display_board(board)

        if player_turn:
            print("Player X's turn")
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
            else:
                print("Cell already taken. Try again.")
                continue
        else:
            print("Player O's turn")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = PLAYER_O
            print(f"AI plays at ({best_move[0]}, {best_move[1]})")

        player_turn = not player_turn

    display_board(board)

    if check_win(board, PLAYER_X):
        print("Player X wins!")
    elif check_win(board, PLAYER_O):
        print("Player O wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()
 