
"""
Matrix Chain Multiplication - Tabulation Approach
"""

from typing import List


def matrix_multiplication(n: int, arr: List[int]) -> int:
    """
    Computes the minimum cost of multiplying matrices using tabulation.

    Args:
        n (int): Number of matrices.
        arr (List[int]): Dimensions of matrices.

    Returns:
        int: Minimum number of scalar multiplications required.
    """
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):  # Length of matrix chain segment
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]
