def lengthOfLIS(nums):
    """
    Calculate the length of the longest increasing subsequence using a dynamic programming approach with a 1D array.

    Args:
        nums (list[int]): A list of integers representing the sequence.

    Returns:
        int: The length of the longest increasing subsequence.

    The function uses a 1D dynamic programming array `dp` where:
        - `dp[i]` represents the length of the longest increasing subsequence that ends at index `i`.
        - The array is initialized to `1` for each element, since the smallest subsequence ending at any index is the element itself.
        - The function iterates over all pairs of elements to check if the current element can form an increasing subsequence with any previous elements.
        - If `nums[i] > nums[j]` (where `i > j`), then we update `dp[i]` to be the maximum of its current value and `dp[j] + 1` (i.e., extending the subsequence ending at index `j`).

    Example:
        For `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the function calculates the longest increasing subsequence length using a 1D DP array.
    """
    n = len(nums)
    dp = [1] * n  # Initialize DP array where each element starts with a subsequence length of 1
    max_len = 1  # To keep track of the longest subsequence found so far

    # Iterate through each element and calculate the longest subsequence ending at that element
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        # Update the maximum length found so far
        if dp[i] > max_len:
            max_len = dp[i]

    # Return the maximum length of the increasing subsequence
    return max_len
