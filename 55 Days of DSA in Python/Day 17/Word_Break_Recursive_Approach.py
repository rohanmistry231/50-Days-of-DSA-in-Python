"""
Word Break Problem - Recursive Approach
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determines if the string `s` can be segmented into space-separated 
    words from the given `word_dict` using recursion.

    Args:
        s (str): Input string.
        word_dict (List[str]): List of valid words.

    Returns:
        bool: True if `s` can be segmented, otherwise False.
    """
    word_set = set(word_dict)  # Convert list to set for optimized lookup
    n = len(s)

    def check_ending_at(index: int) -> bool:
        """
        Recursively checks if `s[:index+1]` can be segmented using words in `word_set`.

        Args:
            index (int): The current ending index to check.

        Returns:
            bool: True if `s[:index+1]` can be segmented, otherwise False.
        """
        if index < 0:
            return True

        for word in word_set:
            word_length = len(word)
            start_idx = index - word_length + 1

            if start_idx >= 0 and s[start_idx:index + 1] == word and check_ending_at(start_idx - 1):
                return True

        return False

    return check_ending_at(n - 1)
