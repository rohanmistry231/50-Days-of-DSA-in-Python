def min_cut(s):
    """
    Find the minimum cuts needed to partition a string into palindromic substrings
    using tabulation (Bottom-Up DP with a 1D DP array).

    Args:
        s (str): The input string.

    Returns:
        int: The minimum number of cuts required.
    """
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    dp = [0] * n

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                is_palindrome[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
            else:
                is_palindrome[i][j] = False

    for end in range(n):
        min_cuts = end
        for start in range(end + 1):
            if is_palindrome[start][end]:
                if start == 0:
                    min_cuts = 0
                else:
                    min_cuts = min(min_cuts, 1 + dp[start - 1])
        dp[end] = min_cuts

    return dp[n - 1]
