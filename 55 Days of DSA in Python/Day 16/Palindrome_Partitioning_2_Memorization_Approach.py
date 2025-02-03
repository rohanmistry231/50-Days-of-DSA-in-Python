def min_cut(s):
    """
    Find the minimum cuts needed to partition a string into palindromic substrings
    using memoization (Top-Down Dynamic Programming).

    Args:
        s (str): The input string.

    Returns:
        int: The minimum number of cuts required.
    """
    n = len(s)
    is_palindrome = [[None] * n for _ in range(n)]
    min_cuts = [[None] * n for _ in range(n)]

    # Precompute palindrome information
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                is_palindrome[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
            else:
                is_palindrome[i][j] = False

    def partitions(start, end):
        """
        Recursively find the minimum cuts for palindromic partitioning with memoization.

        Args:
            start (int): The starting index.
            end (int): The ending index.

        Returns:
            int: The minimum cuts required for partitioning.
        """
        if start == end or is_palindrome[start][end]:
            return 0

        if min_cuts[start][end] is not None:
            return min_cuts[start][end]

        min_cut_count = end - start
        for end_index in range(start, end):
            if is_palindrome[start][end_index]:
                min_cut_count = min(min_cut_count, 1 + partitions(end_index + 1, end))

        min_cuts[start][end] = min_cut_count
        return min_cut_count

    return partitions(0, len(s) - 1)
