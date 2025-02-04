"""
Word Break Problem - Normal DP Approach
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determines if the string `s` can be segmented into space-separated 
    words from the given `word_dict` using dynamic programming.

    Args:
        s (str): Input string.
        word_dict (List[str]): List of valid words.

    Returns:
        bool: True if `s` can be segmented, otherwise False.
    """
    word_set = set(word_dict)  # Convert list to set for optimized lookup
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for length in range(1, n + 1):  # Length of substring
        for start in range(n - length + 1):
            end = start + length - 1

            if s[start:end + 1] in word_set:
                dp[start][end] = True
            else:
                for mid in range(start, end):
                    dp[start][end] = dp[start][end] or (dp[start][mid] and dp[mid + 1][end])

    return dp[0][n - 1]
