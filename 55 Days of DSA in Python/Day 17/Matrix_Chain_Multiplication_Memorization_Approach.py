"""
Matrix Chain Multiplication - Memoization Approach
"""

from typing import List


def matrix_multiplication(n: int, arr: List[int]) -> int:
    """
    Computes the minimum cost of multiplying matrices using memoization.

    Args:
        n (int): Number of matrices.
        arr (List[int]): Dimensions of matrices.

    Returns:
        int: Minimum number of scalar multiplications required.
    """
    dp = [[-1] * n for _ in range(n)]

    def find_cost(i: int, j: int) -> int:
        """
        Helper function to find the minimum multiplication cost using memoization.

        Args:
            i (int): Start index.
            j (int): End index.

        Returns:
            int: Minimum cost of multiplying matrices from i to j.
        """
        if i == j:
            return 0  # Base case: A single matrix has no multiplication cost

        if dp[i][j] != -1:
            return dp[i][j]  # Return precomputed value

        cost = float('inf')
        for k in range(i, j):
            curr_cost = (
                find_cost(i, k) +
                find_cost(k + 1, j) +
                arr[i - 1] * arr[k] * arr[j]
            )
            cost = min(cost, curr_cost)

        dp[i][j] = cost
        return dp[i][j]

    return find_cost(1, n - 1)
