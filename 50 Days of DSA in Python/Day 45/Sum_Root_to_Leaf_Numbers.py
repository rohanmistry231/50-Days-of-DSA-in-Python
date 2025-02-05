class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_root_to_leaf(root, current_sum=0):
    """
    Calculate the sum of all numbers formed from root to leaf.
    """
    if not root:
        return 0
    
    # Update the current sum by appending the current node's value
    current_sum = current_sum * 10 + root.value
    
    # If the node is a leaf, return the current sum
    if not root.left and not root.right:
        return current_sum
    
    # Recursively calculate the sum for the left and right subtrees
    return sum_root_to_leaf(root.left, current_sum) + sum_root_to_leaf(root.right, current_sum)

# Example:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Sum Root to Leaf Numbers:", sum_root_to_leaf(root))
