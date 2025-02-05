class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    """
    Find the lowest common ancestor (LCA) of two nodes in a BST.
    """
    if not root:
        return None
    
    # If both nodes are smaller, go left
    if p.value < root.value and q.value < root.value:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both nodes are larger, go right
    if p.value > root.value and q.value > root.value:
        return lowest_common_ancestor(root.right, p, q)
    
    # Otherwise, root is the LCA
    return root

# Example:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left  # Node 2
q = root.right  # Node 8

print("LCA:", lowest_common_ancestor(root, p, q).value)  # Output: 6
