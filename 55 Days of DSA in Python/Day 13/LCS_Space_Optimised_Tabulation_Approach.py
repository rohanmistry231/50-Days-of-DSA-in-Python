def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the Longest Common Subsequence (LCS) using space optimized tabulation.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the Longest Common Subsequence (LCS).
    """
    n = len(text1)
    m = len(text2)

    # Only store two rows: current and previous
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    # Fill the DP table iteratively, using only the current and previous rows
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        # Move the current row to the previous row for the next iteration
        prev = curr[:]

    # The result is stored in the last cell of the current row
    return curr[m]
