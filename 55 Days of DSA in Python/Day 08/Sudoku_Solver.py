from typing import List

def solve_sudoku(board: List[List[str]]) -> None:
    """
    Solves the Sudoku puzzle in-place.

    Args:
        board (List[List[str]]): A 9x9 2D list representing the Sudoku board.
            Each cell contains a digit '1'-'9' or a '.' for empty cells.

    Returns:
        None: Modifies the board in-place with the solved puzzle.

    Example:
        Input:
        board = [
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

        solve_sudoku(board)

        Output:
        board = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]

    Time Complexity:
        O(9^(n^2)): In the worst case, each cell may try 9 possibilities, with n = 9.

    Space Complexity:
        O(n^2): The recursion stack may go as deep as the total number of cells.
    """

    def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
        """
        Checks if a number can be placed at board[row][col].

        Args:
            board (List[List[str]]): The Sudoku board.
            row (int): Row index.
            col (int): Column index.
            num (str): The number to check.

        Returns:
            bool: True if the number can be placed, False otherwise.
        """
        for x in range(9):
            # Check the row and column
            if board[row][x] == num or board[x][col] == num:
                return False

            # Check the 3x3 sub-grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            r = start_row + x // 3
            c = start_col + x % 3
            if board[r][c] == num:
                return False

        return True

    def backtrack() -> bool:
        """
        Attempts to solve the Sudoku puzzle using backtracking.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if is_valid(board, row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            board[row][col] = "."
                    return False

        return True

    backtrack()

# Example usage
if __name__ == "__main__":
    example_board = [
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

    print("Original Board:")
    for row in example_board:
        print(row)

    solve_sudoku(example_board)

    print("\nSolved Board:")
    for row in example_board:
        print(row)
