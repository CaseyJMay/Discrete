### Implementation of the Minimax algorithm on tic tac toe
from math import inf as infinity

computer = 1 #0
human = -1   #X

def player_wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def check_tie(board):
    #Checks tie by seeeing if all spaces are filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True



def evaluator(board):
    if player_wins(board, human):
        return -10
    elif player_wins(board, computer):
        return 10
    elif check_tie(board):
        return -1
    else:
        return 0

def minimax(board, depth, player):
    score = evaluator(board) * (9-depth)

    if score != 0:
        return score

    if(check_tie(board)):
        return score

    #Maximizer is always the computer
    if player == computer:
        best = -1000000
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = computer

                    best=max(best, minimax(board, depth+1, -player))
                    board[i][j] = 0;
        return best

    elif player == human:
        best = 1000000
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = human

                    best = min(best, minimax(board, depth+1, -player))
                    board[i][j] = 0;
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board[i][j] = computer
                move_score = minimax(board, 0, human)
                board[i][j] = 0

                if (move_score > best_val):
                    best_move = [i, j]
                    best_val = move_score
    return best_move

def render(board):
    """
    Print the board on console
    Board: current state of the board
    """

    chars = {
        -1: "O",
        +1: "X",
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in board:
        for item in row:
            symbol = chars[item]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

if __name__ == "__main__":
    game_board = [
                    [1, 0, 0],
                    [0, 0, -1],
                    [-1, 0, 1]]

    print("input game board:")
    render(game_board)
    move = find_best_move(game_board)

    print("best move:", move)
    game_board[move[0]] [move[1]] = computer
    print("\n\n------------\nupdated game board:")
    render(game_board)

    # print("best move:", move)
    # game_board[move[0]] [move[1]] = computer
    # print("\n\n------------\nupdated game board:")
    # render(game_board)
    #
    # print("best move:", move)
    # game_board[move[0]] [move[1]] = computer
    # print("\n\n------------\nupdated game board:")
    # render(game_board)
