class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_tree(root):
    """
    Calculate the diameter of a binary tree.
    The diameter is the longest path between any two nodes in the tree.
    """
    def helper(node):
        """
        Returns the height of the tree rooted at the given node.
        """
        if not node:
            return 0
        
        # Recursively find the height of left and right subtrees
        left_height = helper(node.left)
        right_height = helper(node.right)
        
        # Update the diameter (longest path seen so far)
        diameter[0] = max(diameter[0], left_height + right_height)
        
        # Return the height of the tree rooted at this node
        return 1 + max(left_height, right_height)
    
    diameter = [0]
    helper(root)
    return diameter[0]

# Example:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of Tree:", diameter_of_tree(root))
