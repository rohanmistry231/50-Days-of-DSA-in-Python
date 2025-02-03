def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using tabulation.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    # Initialize a 2D DP array with dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: if one string is empty, the number of operations is the length of the other string
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill the DP table iteratively
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
            else:
                # Calculate the minimum number of operations
                replace = 1 + dp[i - 1][j - 1]  # Replace character
                delete = 1 + dp[i - 1][j]      # Delete character from word1
                insert = 1 + dp[i][j - 1]      # Insert character into word1
                dp[i][j] = min(replace, delete, insert)  # Choose the minimum operation

    return dp[n][m]
