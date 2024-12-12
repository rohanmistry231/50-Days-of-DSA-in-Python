# Day 8: Backtracking and Classic Constraint Problems

Welcome to Day 8 of **55 Days of DSA in Python**! Today, we delve deeper into **Backtracking**, tackling classic constraint problems like the **Sudoku Solver** and the **N Queens** problem. This README will walk you through the topics, concepts, and solutions covered on this day.

---

### **Topics Covered:**
- Backtracking
- Sudoku Solver
- N Queens

---

## **1. Sudoku Solver**

### **Problem Statement:**
Solve a 9x9 Sudoku puzzle by filling in the empty cells (denoted by `.`) with digits from `1` to `9`. Each digit must satisfy the following constraints:
1. Appears only once in each row.
2. Appears only once in each column.
3. Appears only once in each of the nine 3x3 sub-boxes.

### **Solution Explanation:**
The problem is solved using the backtracking algorithm. The solution involves:
1. Iterating through each empty cell on the board.
2. Trying all possible numbers (`1` to `9`) in the cell.
3. Checking whether the current number placement is valid.
4. If valid, placing the number and recursively solving for the next cell.
5. If no valid placement exists for the current cell, backtracking to the previous cell.

### **Code:**
```python
from typing import List

def solve_sudoku(board: List[List[str]]) -> None:
    """
    Solves a Sudoku puzzle in-place.

    Args:
        board (List[List[str]]): A 9x9 grid where empty cells are represented by `.`.

    Time Complexity:
        O(9^(n*n)): Each empty cell can be filled with one of 9 numbers.

    Space Complexity:
        O(n*n): Board space and recursion stack.

    Example:
        Input: board =
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         ...]
        Output: board =
        [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ...]
    """
    def is_valid(board, row, col, num):
        # Check the row, column, and 3x3 sub-box
        for x in range(9):
            if board[x][col] == num or board[row][x] == num:
                return False
            r = 3 * (row // 3) + x // 3
            c = 3 * (col // 3) + x % 3
            if board[r][c] == num:
                return False
        return True

    def helper():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if helper():
                                return True
                            board[row][col] = '.'
                    return False
        return True

    helper()

# Example Usage:
if __name__ == "__main__":
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solve_sudoku(sudoku_board)
    print("Solved Sudoku Board:")
    for row in sudoku_board:
        print(row)
```

---

## **2. N Queens**

### **Problem Statement:**
Place `n` queens on an `n x n` chessboard such that no two queens threaten each other. Queens can attack horizontally, vertically, and diagonally.

### **Solution Explanation:**
The problem is solved using backtracking:
1. Place a queen in a valid position on the current row.
2. Check if the placement is valid by ensuring no queen threatens another.
3. Move to the next row and repeat.
4. If placing a queen in any column of the current row leads to no solution, backtrack to the previous row.

### **Code:**
```python
from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solves the N-Queens problem and returns all valid configurations.

    Args:
        n (int): The size of the chessboard (n x n).

    Returns:
        List[List[str]]: A list of all valid configurations, where each configuration
        is represented as a list of strings.

    Time Complexity:
        O(n!): The number of permutations to consider.

    Space Complexity:
        O(n^2): Space required for the board and recursion stack.

    Example:
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],
                 ["..Q.","Q...","...Q",".Q.."]]
    """
    def is_valid(row, col, board):
        for x in range(row):
            if board[x][col] == 'Q':
                return False
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c] == 'Q':
                return False
        for r, c in zip(range(row, -1, -1), range(col, n)):
            if board[r][c] == 'Q':
                return False
        return True

    def position_queens(row):
        if row == n:
            res.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_valid(row, col, board):
                board[row][col] = 'Q'
                position_queens(row + 1)
                board[row][col] = '.'

    res = []
    board = [['.'] * n for _ in range(n)]
    position_queens(0)
    return res

# Example Usage:
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Solutions for {n}-Queens:")
    for solution in solutions:
        for row in solution:
            print(row)
        print()
```

---

## **Conclusion**
- **Sudoku Solver**:
  - Efficiently solves Sudoku puzzles using backtracking.
  - Explores all possible placements and backtracks on conflicts.
- **N Queens**:
  - Finds all configurations for placing `n` queens on a chessboard.
  - Utilizes backtracking to explore and validate queen placements.