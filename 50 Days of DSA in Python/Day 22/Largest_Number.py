from functools import cmp_to_key

def largestNumber(nums):
    """
    Arrange numbers to form the largest possible number.

    Args:
        nums (list): A list of non-negative integers.

    Returns:
        str: The largest number formed by concatenating the integers.
    """
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        return 0

    # Convert all integers to strings for custom sorting
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(compare))
    
    # If the largest number is 0, return "0"
    return ''.join(nums) if nums[0] != '0' else '0'
