import numpy as np


def is_valid(board, row, col, num):
    # Check if 'num' is already in the row or column
    if num in board[row, :] or num in board[:, col]:
        return False

    # Check if 'num' is already in the 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[subgrid_row:subgrid_row + 3, subgrid_col:subgrid_col + 3]:
        return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num
                        if solve_sudoku(board):
                            return True
                        board[row, col] = 0
                return False
    return True


# Example Sudoku puzzle as a numpy array
sudoku_board = np.array([
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 2, 0, 0, 6, 3, 0],
    [0, 8, 2, 1, 0, 0, 0, 0, 9],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [5, 0, 0, 0, 9, 0, 1, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 8, 0],
    [0, 0, 0, 9, 0, 0, 0, 6, 0],
    [0, 0, 1, 7, 2, 0, 4, 0, 0]
], dtype=int)

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print(sudoku_board)
else:
    print("No solution exists.")
