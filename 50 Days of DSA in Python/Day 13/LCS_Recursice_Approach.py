def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the Longest Common Subsequence (LCS) using recursion.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the Longest Common Subsequence (LCS).
    """
    n = len(text1)
    m = len(text2)

    def helper(index1, index2):
        # Base case: If either string has been fully processed
        if index1 >= n or index2 >= m:
            return 0

        # If characters match, include them in the LCS
        if text1[index1] == text2[index2]:
            return 1 + helper(index1 + 1, index2 + 1)
        
        # Otherwise, explore both possibilities (skip character from either text1 or text2)
        return max(helper(index1 + 1, index2), helper(index1, index2 + 1))

    return helper(0, 0)
