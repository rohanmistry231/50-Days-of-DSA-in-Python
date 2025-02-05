def maxArea(height):
    """
    Calculate the maximum area that can be formed between two lines.

    Args:
        height (list): A list of integers representing the heights of lines.

    Returns:
        int: The maximum area formed by any two lines.
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the current pair of lines
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
