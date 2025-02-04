def min_cut(s):
    """
    Find the minimum cuts needed to partition a string into palindromic substrings
    using tabulation (Bottom-Up Dynamic Programming).

    Args:
        s (str): The input string.

    Returns:
        int: The minimum number of cuts required.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = 0
            elif s[i] == s[j] and (dp[i + 1][j - 1] == 0):
                dp[i][j] = 0
            else:
                dp[i][j] = j - i
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 1 + dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]
