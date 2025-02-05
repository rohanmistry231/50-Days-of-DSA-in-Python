def searchMatrix(matrix, target):
    """
    Search for the target value in a 2D matrix.

    Args:
        matrix (list of list): A 2D matrix where each row is sorted.
        target (int): The target value to search for.

    Returns:
        bool: True if the target is found in the matrix, False otherwise.
    """
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False
