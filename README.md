# 🔢 Sudoku Solver (with NumPy)

A Python script that solves 9x9 Sudoku puzzles using a recursive backtracking algorithm. This project is part of a collection of NumPy-focused learning projects.

---

## 🧠 How It Works

The puzzle is represented as a 9x9 NumPy array, with empty cells marked as `0`. The algorithm:

1. Finds the next empty cell
2. Tries placing numbers `1–9` into that cell
3. Checks if the number is valid (row, column, 3x3 box)
4. Recursively continues until the puzzle is solved

If a placement leads to a dead end, the algorithm backtracks and tries a new number.

---

## 🚀 How to Run

1. Clone the repo or copy this folder into your workspace
2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Install NumPy:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
    ```bash
    python sudoku_solver.py
    ```

---

## 📦 Requirements

Only NumPy is required:

## 🏗️ Future Ideas

- Add support for different grid sizes
- Build a GUI with tkinter or PyGame
- Add a generator to create puzzles


## Sample Output

Sudoku Puzzle:
5 3 0  | 0 7 0  | 0 0 0
6 0 0  | 1 9 5  | 0 0 0
0 9 8  | 0 0 0  | 0 6 0
---------------------
8 0 0  | 0 6 0  | 0 0 3
4 0 0  | 8 0 3  | 0 0 1
7 0 0  | 0 2 0  | 0 0 6
---------------------
0 6 0  | 0 0 0  | 2 8 0
0 0 0  | 4 1 9  | 0 0 5
0 0 0  | 0 8 0  | 0 7 9

Note: 0 means empty space

✅ Solved Sudoku:
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
---------------------
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
---------------------
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9