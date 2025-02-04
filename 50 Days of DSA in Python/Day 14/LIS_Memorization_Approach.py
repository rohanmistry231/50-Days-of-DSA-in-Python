def lengthOfLIS(nums):
    """
    Calculate the length of the longest increasing subsequence using memoization.

    Args:
        nums (list[int]): A list of integers representing the sequence.

    Returns:
        int: The length of the longest increasing subsequence.
    """
    n = len(nums)
    dp = [[-1] * n for _ in range(n)]

    def helper(curr, prev):
        # Base case: if the current index exceeds the array length
        if curr > n - 1:
            return 0

        # If the result has already been computed, return the cached value
        if dp[curr][prev + 1] != -1:
            return dp[curr][prev + 1]

        # Exclude the current element from the subsequence
        exclude = helper(curr + 1, prev)

        # Include the current element if it forms an increasing subsequence
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)

        # Store the result in the dp table and return it
        dp[curr][prev + 1] = max(include, exclude)
        return dp[curr][prev + 1]

    return helper(0, -1)
