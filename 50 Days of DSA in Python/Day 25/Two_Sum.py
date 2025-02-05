def twoSum(nums, target):
    """
    Find two numbers in the list that add up to the target using a hash table.

    Args:
        nums (list): List of integers.
        target (int): The target sum.

    Returns:
        list: Indices of the two numbers.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
