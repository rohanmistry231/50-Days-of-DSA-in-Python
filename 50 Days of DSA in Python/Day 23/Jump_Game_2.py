def jump(nums):
    """
    Calculate the minimum number of jumps to reach the last index.

    Args:
        nums (list): A list of non-negative integers representing maximum jumps.

    Returns:
        int: The minimum number of jumps required to reach the last index.
    """
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps
