"""
Tic Tac Toe Player
"""

import math
import copy

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
    if terminal(board):
        return X 
    elif board == initial_state():
        return X

    c = 0
    for i in range(len(board)):
        c += board[i].count(None)
    if c & 1==1:
        c += 1
        return X
    if c & 1==0:
        c += 1
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return {(2,2)} 
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions           

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not valid(action):
        raise Exception("not valid action")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
        return new_board

def valid(action):
    if 0 <= action[0] <=2 and 0 <= action[1] <=2:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    dig = 1
    sdig = 1
    clu = 1
    ro = 1
    for i in range(3):
        clu = 1
        for j in range(3):
            if board[i][j] == None:
                continue
            if j+1<3 and board[i][j] == board[i][j+1]:
                clu += 1
                if clu == 3:
                    return (X if board[i][j]=="X" else O)
            if i+1<3 and j+1<3 and i==j and board[i][j] == board[i+1][j+1]:
                dig += 1
                if dig == 3:
                    return X if board[i][j]=="X" else O
    for j in range(2):
        ro = 1
        for i in range(2):
            if board[i][j] == None:
                continue
            if i+1<3 and board[i][j] == board[i+1][j]:
                ro += 1
                if ro == 3:
                    return X if board[i][j]=="X" else O

    for i in range(0, 2):
        if board[i][j] == None:
            continue
        j = 2-i
        if board[i][j] == board[i+1][j-1]:
            sdig += 1
            if sdig == 3:
                return X if board[i][j]=="X" else O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    v = float("inf")
    opt = ()
    if player(board) == "O":
        for act in actions(board):
            if v != min(v, max_value(result(board, act))):
                v = min(v, max_value(result(board, act)))
                opt = act
        return opt 

    v = float("-inf")
    if player(board) == "X":
        for act in actions(board):
            if v != max(v, min_value(result(board, act))):
                v = max(v, min_value(result(board, act)))
                opt = act
        return opt 
    #     maxm = -3487
    #     opt = ()
    #     for act in actions(board):
    #     mnm = 3487
    #     opt = ()
    #     for act in actions(board):
    #         if mnm != min(mnm, min_value(board, act)):
    #             mnm = min(mnm, min_value(board, act))
    #             opt = act
    #     return opt
        
def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for act in actions(board):
        v = min(v,max_value(result(board, act)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for act in actions(board):
        v = max(v, min_value(result(board, act)))
    return v
