import numpy as np

def print_board(board):
    """Pretty-print the Sudoku board with row and column dividers."""
    for i in range(9):
        row = ''
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += ' | '
            row += str(board[i][j]) + ' '
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print('-' * 21)

def find_empty(board):
    """Find the next empty cell (value = 0). Return (row, col) or None if full."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    """
    Check if placing 'num' at position 'pos' is valid:
    - not in the same row
    - not in the same column
    - not in the same 3x3 box
    """
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in board[:, col]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    box = board[box_y*3:box_y*3+3, box_x*3:box_x*3+3]
    if num in box:
        return False

    return True

def solve(board):
    """
    Solve the Sudoku puzzle using recursion and backtracking.
    Modify the board in place and return True if solved.
    """
    empty = find_empty(board)
    if not empty:
        return True  # Base case: no empty cells left → solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Try placing the number

            if solve(board):
                return True  # If success, return up the chain

            board[row][col] = 0  # If not, backtrack

    return False  # Trigger backtracking

# 🧪 Run the solver
if __name__ == "__main__":
    # Sample Sudoku board with 0s as empty spaces
    board = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    print("Sudoku Puzzle:")
    print_board(board)

    if solve(board):
        print("\n✅ Solved Sudoku:")
        print_board(board)
    else:
        print("❌ No solution exists.")
