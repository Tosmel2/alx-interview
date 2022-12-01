#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    dimension = int(sys.argv[1])
except Exception as E:
    print("N must be a number")
    exit(1)

if dimension < 4:
    print("N must be at least 4")
    exit(1)

board = {}
for row in range(0, dimension):
    for column in range(0, dimension):
        placement = (row, column)
        board[placement] = "#"


def validate(board, spots):
    """ Valitate the board """
    if len([i for i in board.values() if i == "#"]) < spots and spots != 0:
        return False
    return True


def solve(dimension, index, board, safe_T, spots_L):
    """ main loop for recursive """
    if len(safe_T) > dimension:
        return False
    moved_board = fill_block(dimension, index, board)
    if validate(moved_board, spots_L) and moved_board:
        spots_L -= 1
        inital = (index[0] + 1, index[1])
        for i in range(dimension):
            try:
                if moved_board[(inital[0], i)] == "#":
                    safe_T.append([inital[0], i])
                    if not solve(
                            dimension, (inital[0], i), moved_board,
                            safe_T, spots_L):
                        safe_T.pop()
                        continue
            except BaseException:
                continue
    if spots_L < 0 and len(safe_T) == dimension:
        print(safe_T)
    else:
        return False


def fill_block(dimension, index, board_T):
    """ function to fill queens available spots """
    board = board_T.copy()
    board[index] = 0
    diagonal_C_neg_x = []
    diagonal_C_pos_x = []
    diagonal_C_neg_y = []
    diagonal_C_pos_y = []
    x = index[1]
    while x - 1 >= 0:
        less_x = (index[0], x - 1)
        diagonal_C_neg_x.append(x - 1)
        if board.get(less_x) == 0:
            return False
        board[less_x] = 1
        x -= 1

    y = index[0]
    while y - 1 >= 0:
        less_y = (y - 1, index[1])
        diagonal_C_neg_y.append(y - 1)
        if board.get(less_y) == 0:
            return False
        board[less_y] = 1
        y -= 1

    x = index[1]
    while x + 1 < dimension:
        more_x = (index[0], x + 1)
        diagonal_C_pos_x.append(x + 1)
        if board.get(more_x) == 0:
            return False
        board[more_x] = 1
        x += 1

    y = index[0]
    while y + 1 < dimension:
        more_y = (y + 1, index[1])
        diagonal_C_pos_y.append(y + 1)
        if board.get(more_y) == 0:
            return False
        board[more_y] = 1
        y += 1

    upper_left = tuple(zip(diagonal_C_pos_y, diagonal_C_neg_x))
    upper_right = tuple(zip(diagonal_C_pos_y, diagonal_C_pos_x))
    lower_left = tuple(zip(diagonal_C_neg_y, diagonal_C_neg_x))
    lower_right = tuple(zip(diagonal_C_neg_y, diagonal_C_pos_x))
    for ind in (upper_left + upper_right + lower_left + lower_right):
        if board.get(ind) == 0:
            return False
        board[ind] = 1
    return board


for i in range(0, dimension):
    inital = (0, i)
    safe_T = [list(inital)]
    spots_L = dimension - 1
    solve(dimension, inital, board, safe_T, spots_L)
