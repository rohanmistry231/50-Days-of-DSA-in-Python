def count_substrings(s):
    """
    This function counts the number of palindromic substrings in the given string using recursion.

    Args:
    s (str): The input string to check for palindromic substrings.

    Returns:
    int: The number of palindromic substrings in the input string.
    """
    n = len(s)
    dp = [[-1] * n for _ in range(n)]

    def helper(i, j):
        """
        A helper function that recursively checks whether the substring s[i:j+1] is a palindrome.

        Args:
        i (int): The starting index of the substring.
        j (int): The ending index of the substring.

        Returns:
        bool: True if s[i:j+1] is a palindrome, False otherwise.
        """
        # Base case: single character is always a palindrome
        if i == j:
            dp[i][j] = True
            return dp[i][j]

        # If we've already computed the value for this substring, return it
        if dp[i][j] != -1:
            return dp[i][j]

        # Recursively check for smaller substrings
        helper(i + 1, j)
        helper(i, j - 1)

        # Check if current substring is a palindrome
        if s[i] == s[j] and (j == i + 1 or helper(i + 1, j - 1)):
            dp[i][j] = True
        else:
            dp[i][j] = False

        return dp[i][j]

    # Start by processing the entire string
    helper(0, n - 1)

    # Count how many substrings are palindromes
    result = 0
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i][j] is True:
                result += 1
    return result
