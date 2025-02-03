def lengthOfLIS(nums):
    """
    Calculate the length of the longest increasing subsequence using recursion.

    Args:
        nums (list[int]): A list of integers representing the sequence.

    Returns:
        int: The length of the longest increasing subsequence.
    """
    n = len(nums)

    def helper(curr, prev):
        # Base case: if the current index exceeds the array length
        if curr > n - 1:
            return 0

        # Exclude the current element from the subsequence
        exclude = helper(curr + 1, prev)

        # Include the current element if it forms an increasing subsequence
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)

        # Return the maximum of including or excluding the current element
        return max(include, exclude)

    return helper(0, -1)
