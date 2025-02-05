class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    """
    Convert a sorted array to a height-balanced BST.
    """
    if not nums:
        return None
    
    # Find the middle element to be the root
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    # Recursively build the left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root

# Example:
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)
