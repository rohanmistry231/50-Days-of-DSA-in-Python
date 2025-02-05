def searchRange(nums, target):
    """
    Find the first and last position of the target in a sorted array.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        list: A list with the first and last positions of the target value.
    """
    
    def findLeft():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findRight():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    left, right = findLeft(), findRight()
    
    if left <= right:
        return [left, right]
    return [-1, -1]
