class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    """
    Constructs a binary tree from pre-order and in-order traversal lists.
    """
    def helper(preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # The first element of preorder is the root
        root_value = preorder[0]
        root = TreeNode(root_value)
        
        # Find the root in inorder to split left and right subtrees
        root_index = inorder.index(root_value)
        
        # Recursively build the left and right subtrees
        root.left = helper(preorder[1:1 + root_index], inorder[:root_index])
        root.right = helper(preorder[1 + root_index:], inorder[root_index + 1:])
        
        return root
    
    return helper(preorder, inorder)

# Example:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)