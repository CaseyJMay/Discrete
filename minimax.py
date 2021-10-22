### Implementation of the Minimax algorithm on tic tac toe

computer = 1
human = -1

game_board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def game_finished(state, player):
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

#function to find the best possible move given the current game board
def best_move(board):
    #implementation can utilize minimax
    return None

def minimax(board, depth, isMaximizer):
    if isEndGame():
        return board
    elif isMaximizer:
        #determine current value
        #determine whether another choice is better
        #recurse
        #return better choice
    else:
        #recurse to 1 higher depth

#determines whether the game has reached the end game state
#based on # of remaining unfilled squares and also whether a
#winning state has been reached.
def isEndGame():
    return None
