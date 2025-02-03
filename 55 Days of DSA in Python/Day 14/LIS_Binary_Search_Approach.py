def lengthOfLIS(nums):
    """
    Calculate the length of the longest increasing subsequence using a binary search approach.

    Args:
        nums (list[int]): A list of integers representing the sequence.

    Returns:
        int: The length of the longest increasing subsequence.

    The function uses a binary search to find the position of the current number in the `sub` array, which keeps track
    of the smallest possible tail element for all increasing subsequences of different lengths.

    Steps:
        1. Start with the first element of the list in `sub`, which represents the first subsequence.
        2. For each subsequent element in `nums`:
            - If the element is greater than the last element of `sub`, append it to `sub`.
            - If the element is smaller or equal to the last element of `sub`, find the position in `sub` where this
              element should be placed using binary search. Replace the element at that position.
        3. The length of the `sub` array at the end of the process will represent the length of the longest increasing subsequence.

    Example:
        For `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the binary search approach efficiently calculates the longest increasing subsequence length.
    """
    def binarySearch(sub, num):
        """
        Perform binary search to find the correct position of `num` in `sub` array.
        
        Args:
            sub (list[int]): A list representing the subsequence so far.
            num (int): The number to be inserted or replaced in `sub`.
        
        Returns:
            int: The index at which `num` should be placed in `sub`.
        """
        left = 0
        right = len(sub) - 1
        while left < right:
            mid = (left + right) // 2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left

    if not nums:
        return 0

    # `sub` will store the smallest possible tail element for increasing subsequences
    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            index = binarySearch(sub, num)
            sub[index] = num

    return len(sub)
