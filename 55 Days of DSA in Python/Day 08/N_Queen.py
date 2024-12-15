from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solve the N-Queens problem and return all distinct solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        List[List[str]]: A list of solutions, where each solution is represented as a list of strings.

    Example:
        Input: n = 4
        Output: [
            [".Q..",  "...Q",  "Q...",  "..Q."],
            ["..Q.",  "Q...",  "...Q",  ".Q.."]
        ]

    Time Complexity:
        O(n!): The number of permutations of placing queens on the board decreases with pruning.

    Space Complexity:
        O(n^2): The space required to store the board and recursion stack.
    """
    solutions = []

    def create_board(board: List[List[str]]) -> List[str]:
        """
        Convert the board from a list of lists to a list of strings.

        Args:
            board (List[List[str]]): The board as a 2D list.

        Returns:
            List[str]: The board as a list of strings.
        """
        return ["".join(row) for row in board]

    def is_valid(row: int, col: int, board: List[List[str]]) -> bool:
        """
        Check if placing a queen at board[row][col] is valid.

        Args:
            row (int): The row index.
            col (int): The column index.
            board (List[List[str]]): The current state of the board.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Check column
        for r in range(row):
            if board[r][col] == 'Q':
                return False

        # Check top-left diagonal
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c] == 'Q':
                return False

        # Check top-right diagonal
        for r, c in zip(range(row, -1, -1), range(col, n)):
            if board[r][c] == 'Q':
                return False

        return True

    def place_queens(board: List[List[str]], row: int) -> None:
        """
        Recursively attempt to place queens on the board.

        Args:
            board (List[List[str]]): The current state of the board.
            row (int): The current row to place a queen.
        """
        # Base case: All queens are placed
        if row == n:
            solutions.append(create_board(board))
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(row, col, board):
                # Place the queen
                board[row][col] = 'Q'

                # Recurse to the next row
                place_queens(board, row + 1)

                # Backtrack by removing the queen
                board[row][col] = '.'

    # Initialize the board
    initial_board = [['.'] * n for _ in range(n)]

    # Start placing queens from the first row
    place_queens(initial_board, 0)

    return solutions

# Example usage
if __name__ == "__main__":
    n_value = 4
    result = solve_n_queens(n_value)
    print(f"Solutions for {n_value}-Queens problem:")
    for solution in result:
        for row in solution:
            print(row)
        print()