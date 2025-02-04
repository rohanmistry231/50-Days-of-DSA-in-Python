def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the Longest Common Subsequence (LCS) using tabulation.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the Longest Common Subsequence (LCS).
    """
    n = len(text1)
    m = len(text2)

    # Initialize a DP table with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table iteratively
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, include them in the LCS
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            # If characters don't match, take the maximum of excluding one character from either string
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell contains the length of the LCS
    return dp[n][m]
