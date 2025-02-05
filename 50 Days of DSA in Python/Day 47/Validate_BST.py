class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    """
    Validate if a binary tree is a valid BST.
    """
    if not root:
        return True
    
    # Check if current node value is within the valid range
    if not (low < root.value < high):
        return False
    
    # Recursively check the left and right subtrees with updated bounds
    return is_valid_bst(root.left, low, root.value) and is_valid_bst(root.right, root.value, high)

# Example:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print("Is the tree a valid BST?", is_valid_bst(root))  # Output: True
