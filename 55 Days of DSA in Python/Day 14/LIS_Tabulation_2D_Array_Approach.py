def lengthOfLIS(nums):
    """
    Calculate the length of the longest increasing subsequence using tabulation (bottom-up dynamic programming).

    Args:
        nums (list[int]): A list of integers representing the sequence.

    Returns:
        int: The length of the longest increasing subsequence.

    The function uses a 2D dynamic programming table `dp` where:
        - `dp[i][j]` represents the length of the longest increasing subsequence in the subarray from index `i` to `j`.
        - The table is initialized as a 2D array with dimensions `(n+1) x (n+1)` where `n` is the length of the input list `nums`.
        - The table is filled by iterating backward over the array:
            - `exclude` refers to not including the current element (`nums[i]`), i.e., considering the subarray starting from the next index (`i + 1`).
            - `include` refers to including the current element, which is valid if `nums[i] > nums[j-1]`.
        - The final value at `dp[0][0]` gives the length of the longest increasing subsequence in the entire list `nums`.

    Example:
        For `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the function calculates the longest increasing subsequence length using a 2D DP table.
    """
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize 2D dp table

    # Fill the dp table by iterating from the end of the array to the beginning
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            # Exclude the current element
            exclude = dp[i + 1][j]

            # Include the current element if it forms an increasing subsequence
            include = 0
            if j - 1 == -1 or nums[i] > nums[j - 1]:
                include = 1 + dp[i + 1][i + 1]

            # Store the maximum of including or excluding the current element
            dp[i][j] = max(exclude, include)

    # Return the length of the longest increasing subsequence
    return dp[0][0]
