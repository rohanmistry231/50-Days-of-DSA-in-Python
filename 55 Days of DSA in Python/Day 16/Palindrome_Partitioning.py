def partition(s):
    """
    Partition a string into all possible palindromic substrings.

    Args:
        s (str): The input string to partition.

    Returns:
        List[List[str]]: A list of lists, where each list contains a valid partition of palindromic substrings.
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Fill the DP table to check if substrings are palindromes
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                dp[i][j] = True

    def backtrack(index, current_partition):
        """
        Helper function to perform backtracking for palindrome partitioning.

        Args:
            index (int): The starting index for the current partition.
            current_partition (List[str]): The current list of palindromic substrings.
        """
        # Base case: If index exceeds the string length, add partition to result
        if index == n:
            result.append(current_partition[:])
            return

        # Explore all partitions starting from current index
        for i in range(index, n):
            if dp[index][i]:
                current_partition.append(s[index:i + 1])
                backtrack(i + 1, current_partition)
                current_partition.pop()

    result = []
    backtrack(0, [])
    return result
