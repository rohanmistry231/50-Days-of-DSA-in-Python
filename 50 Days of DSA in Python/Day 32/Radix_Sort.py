def radixSort(nums):
    """
    Sort the list using Radix Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) == 0:
        return nums

    # Find the maximum number to know the number of digits
    max_num = max(nums)
    place = 1  # Start with the least significant digit
    
    while max_num // place > 0:
        nums = countingSortByDigit(nums, place)
        place *= 10

    return nums

def countingSortByDigit(nums, place):
    """
    Perform Counting Sort based on the digit represented by 'place'.

    Args:
        nums (list): The list of integers to be sorted.
        place (int): The digit place (1 for ones, 10 for tens, etc.).

    Returns:
        list: The list sorted by the digit at 'place'.
    """
    output = [0] * len(nums)
    count = [0] * 10

    # Store count of occurrences in count[]
    for num in nums:
        index = num // place % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output list
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        index = num // place % 10
        output[count[index] - 1] = num
        count[index] -= 1

    return output
