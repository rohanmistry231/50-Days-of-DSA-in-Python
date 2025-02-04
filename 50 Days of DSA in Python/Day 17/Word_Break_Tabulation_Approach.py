"""
Word Break Problem - Tabulation (Bottom-Up DP) Approach
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determines if the string `s` can be segmented into space-separated 
    words from the given `word_dict` using a bottom-up DP approach.

    Args:
        s (str): Input string.
        word_dict (List[str]): List of valid words.

    Returns:
        bool: True if `s` can be segmented, otherwise False.
    """
    word_set = set(word_dict)  # Convert list to set for faster lookups
    n = len(s)
    dp = [False] * n  # DP table where dp[i] represents if s[:i+1] is segmentable

    for i in range(n):
        for word in word_set:
            word_length = len(word)

            if i < word_length - 1:
                continue

            start_idx = i - word_length + 1
            if s[start_idx:i + 1] == word and (start_idx == 0 or dp[start_idx - 1]):
                dp[i] = True
                break

    return dp[n - 1]
